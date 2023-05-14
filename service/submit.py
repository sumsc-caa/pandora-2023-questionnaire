from .base import blueprint, render_template, error_page
from questionnaire import Questionnaire
from components import FormValueError
from flask import request
from database import Database
import json


@blueprint.route("/submit/<int:qid>", methods=['POST'])
def submitQuestionnaire(qid: int):
    data = request.form
    print(data)
    q = Questionnaire.get_questionnaire(qid)
    if q is None:
        return error_page("问卷不存在", 404)
    try:
        result = q.parse(data)
    except FormValueError as e:
        return error_page(e.message)

    print(result)

    # 数据入库，放在formvalue表内，result使用json编码后存储
    with Database() as db:
        result = db.execute(
            "INSERT INTO formvalue (qid, value) VALUES (?, ?)",
            (qid, json.dumps(result))
        )
        db.commit()

    return submitSuccess(q.qid, q.name)


def submitSuccess(qid: int, qname: str,
                  message: str = "感谢您抽出时间参与我们的调查", jump="/"):
    return render_template(
        "success.html", qid=qid, qname=qname, message=message, jump=jump)
