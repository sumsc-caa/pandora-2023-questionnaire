from .base import blueprint, render_template, error_page
from questionnaire import Questionnaire

@blueprint.route("/view/<int:qid>")
def tableview(qid: int):
    """数据展示页，展示网站收集到的答卷"""
    q = Questionnaire.get_questionnaire(qid)
    if q is None:
        return error_page("问卷不存在", 404)

    # TODO(Stage 2): 从数据库获得数据

    return render_template("tableview.html") # 展示的部分暂时不搞
