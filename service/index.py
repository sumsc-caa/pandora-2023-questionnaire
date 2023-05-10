from .base import blueprint, render_template


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
    # TODO: 获取系统里的所有问卷，返回上述信息

    return render_template(
        "index.html",
        questionnaires=[(1, "name", "description", 10),
                        (2, "测试问卷", "用来测试的问卷哦", 20)]
    )
