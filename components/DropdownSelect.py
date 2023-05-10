from .BaseComponent import BaseComponent, Template, register_component
from .BaseComponent import ImmutableMultiDict

# 添加装饰器使程序能加载并注册这个组件


@register_component
class DropdownSelect(BaseComponent):
    """下拉选择框
    参考：https://getbootstrap.com/docs/5.2/forms/select/
    """
    # TODO: 完善组件

    template = Template("")

    def render(self,
               index: int,
               name: str,
               caption: str,
               options: list[tuple[str, str]],
               placeholder: str = "",
               required=True,
               desc: str = "",
               **_):
        """
        Args:
            index (int): 问题序号
            name (str): 问题名称（存储时使用）
            caption (str): 问题题干
            option (list[(key: str, value: str)]): 问题的选项
                key (str): 该项的键（存入表单的值）
                value (str): 该项的展示值（渲染时展示的值）
            placeholder (str, optional): 输入提示. Defaults to "".
            required (bool, optional): 是否必须. Defaults to True.
            desc (str, optional): 字段描述. Defaults to "".

        Returns:
            str: 渲染好的问卷
        """

    # ruff: noqa: F811
    render = BaseComponent.render  # 编写时删去此行

    def parse(self,
              name: str,
              formdata: ImmutableMultiDict,
              qdata=None,
              datatype='str',
              validation=None):
        # TODO
        # ? 验证一下是否用户所选都在问题提供的选项内
        return super().parse(name, formdata, qdata, datatype, validation)
