from .base import blueprint, render_template

@blueprint.route("/")
def index():
    """展示系统里的所有问卷

    Returns:
        questionnaires (list[(qid: int, name: str, desc: str, count: int)]): 所有问卷的列表，其中：
            qid (int): 问卷qid
            name (str): 问卷名
            desc (str): 问卷简介
            count (int): 该问卷当前的答卷数量
    """
    # TODO: 编写主页
    # TODO: 获取系统里的所有问卷
    
    return render_template("index.html", questionnaires = [(1, "name", "description", 10)])