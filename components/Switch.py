from .BaseComponent import BaseComponent, Template, register_component
from .BaseComponent import ImmutableMultiDict

# 添加装饰器使程序能加载并注册这个组件


@register_component
class Switch(BaseComponent):
    """开关
    参考：https://getbootstrap.com/docs/5.2/forms/checks-radios/#switches
    """
    # TODO: 完善组件

    template = Template("")

    def render(self,
               index: int,
               name: str,
               caption: str,
               default=False,
               required=True,
               desc: str = "",
               **_):
        """开关

        Args:
            index (int): 问题序号
            name (str): 问题名称（存储时使用）
            caption (str): 问题题干
            default (bool): 默认值
            required (bool): 是否必须
            desc (str): 问题描述
        """

    # ruff: noqa: F811
    render = BaseComponent.render  # 编写时删去此行

    def parse(self,
              name: str,
              formdata: ImmutableMultiDict,
              qdata=None,
              datatype='bool',
              validation=None):
        # TODO
        return super().parse(name, formdata, qdata, datatype, validation)
