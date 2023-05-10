from .base import blueprint, render_template, error_page
from questionnaire import Questionnaire


@blueprint.route("/questionnaire/<int:qid>")
def renderQuestionnaire(qid: int):
    """渲染表单"""
    q = Questionnaire.get_questionnaire(qid)
    if q is None:
        return error_page("问卷不存在", 404)

    return render_template(
        "questionnaire.html", queries=q.render(), qid=q.qid, qname=q.name, desc=q.desc)
