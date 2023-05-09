from .base import blueprint, render_template

@blueprint.route("/view/<int:qid>")
def dataview(qid: int):
    """数据展示页，展示网站收集到的答卷"""
    # TODO: 从数据库获得数据
    # TODO: 渲染页面
    
    return render_template("dataview.html")