from flask import Blueprint
from flask import render_template

blueprint = Blueprint('api', __name__)


@blueprint.route("/error")  # for tests only
def error_page(errmsg: str = "测试错误", status_code: int = 400, jump: str = "/"):
    """渲染错误页

    Args:
        errmsg (str): 错误信息
        status_code (int, optional): HTML status code. Defaults to 400.
        jump (str, optional): 跳转目标
    """

    return render_template("errorpage.html",
                           errmsg=errmsg,
                           jump=jump,
                           status_code=status_code
                           ), status_code
