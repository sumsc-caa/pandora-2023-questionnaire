from .base import blueprint, render_template
from database import Database

@blueprint.route("/")
@blueprint.route("/index")
@blueprint.route("/index.html")
def index():
    """展示系统里的所有问卷

    Returns:
        questionnaires (list[(qid:int, name:str, desc:str, count:int)]): 所有问卷的列表
            qid (int): 问卷qid
            name (str): 问卷名
            desc (str): 问卷简介
            count (int): 该问卷当前的答卷数量
    """
    # 获取系统里的所有问卷，返回上述信息
    with Database() as db:
        result = db.execute('''
            SELECT questionnaire.qid, name, desc,
                COALESCE(COUNT(formvalue.id), 0) AS count
            FROM questionnaire
            LEFT JOIN formvalue ON questionnaire.qid = formvalue.qid
            GROUP BY questionnaire.qid
        ''').fetchall()

    return render_template(
        "index.html",
        questionnaires=result
    )
