from .base import blueprint, request


@blueprint.route("/submit/<int:qid>", methods=['POST'])
def submitQuestionnaire(qid: int):
    data = request.form
    print(data)
    # TODO: 数据入库
    # TODO: 做个美观的提交成功页
    
    return "提交成功"