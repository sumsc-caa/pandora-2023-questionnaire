from .BaseComponent import BaseComponent, Template, register_component
from .BaseComponent import ImmutableMultiDict

# 添加装饰器使程序能加载并注册这个组件


@register_component
class Textarea(BaseComponent):
    """多行文本框
    参考：https://getbootstrap.com/docs/5.2/forms/form-control/#example
    """

    template = Template("")

    def render(self,
               index: int,
               name: str,
               caption: str,
               placeholder: str = "",
               default="",
               required=True,
               desc: str = "",
               **_):
        """多行文本框

        Args:
            index (int): 问题序号
            name (str): 问题的名称
            caption (str): 问题题干
            placeholder (str, optional): 输入提示. Defaults to "".
            default (str, optional): 默认值
            required (bool, optional): 是否必须. Defaults to True.
            desc (str, optional): 字段描述. Defaults to "".
        """
        # ? 加分项：在文本框下显示实时字数统计（需要Javascript，加1分）
        # ? 加分项：实时字数限制与相应提示（例：边框变红）（需要Javascript，加1分）

    # ruff: noqa: F811
    render = BaseComponent.render  # 编写时删去此行

    def parse(self,
              name: str,
              formdata: ImmutableMultiDict,
              qdata=None,
              datatype='str',
              validation=None):
        return super().parse(name, formdata, qdata, datatype, validation)
