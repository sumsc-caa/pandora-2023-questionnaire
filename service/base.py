from flask import Blueprint
from flask import render_template
from flask import request

blueprint = Blueprint('api', __name__)


def error_page(errmsg: str, status_code: int = 400, jump: str = "/"):
    """错误页

    Args:
        errmsg (str): 错误信息
        status_code (int, optional): HTML status code. Defaults to 400.
        jump (str, optional): 跳转目标
    """
    # TODO: 做一个更好的错误页
    
    return errmsg, status_code