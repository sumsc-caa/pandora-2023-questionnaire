from .BaseComponent import BaseComponent, Template, register_component
from .BaseComponent import ImmutableMultiDict

# 添加装饰器使程序能加载并注册这个组件


@register_component
class Range(BaseComponent):
    """Slider
    参考：https://getbootstrap.com/docs/5.2/forms/range/
    """
    # TODO: 完善组件

    template = Template("")

    def render(self,
               index: int,
               name: str,
               caption: str,
               min=0,
               max=10,
               step=1,
               required=True,
               desc: str = "",
               **_):
        """开关

        Args:
            index (int): 问题序号
            name (str): 问题名称（存储时使用）
            caption (str): 问题题干
            min (int | float): 下限
            max (int | float): 上限
            step (int | float): 步长
            required (bool): 是否必须
            desc (str): 问题描述
        """
        # ? 加分项：在组件右侧展示当前选中的值（需要JavaScript，加1分）

    # ruff: noqa: F811
    render = BaseComponent.render  # 编写时删去此行

    def parse(self,
              name: str,
              formdata: ImmutableMultiDict,
              qdata=None,
              datatype='float',
              validation=None):
        # TODO
        return super().parse(name, formdata, qdata, datatype, validation)
