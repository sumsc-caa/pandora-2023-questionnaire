from werkzeug.datastructures import ImmutableMultiDict
from .BaseComponent import BaseComponent, Template, register_component

# 添加装饰器使程序能加载并注册这个组件


@register_component
class BoxSelect(BaseComponent):
    """多选框
    参考：https://getbootstrap.com/docs/5.2/forms/checks-radios/#checks
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
        """多选框

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
        # ? 可以在此基础上添加其他功能，例如最少选择m项，最多选择n项等

    # ruff: noqa: F811
    render = BaseComponent.render  # 编写时删去此行

    def parse(self,
              name: str,
              formdata: ImmutableMultiDict,
              qdata=None,
              datatype='str',
              validation=None):
        # TODO
        # ? 验证一下是否用户所选项都在问题提供的选项内
        # ? 需要返回一个列表，里面是用户选中的所有项
        # ? 提示：ImmutableMultiDict 有一个 getlist 方法
        return super().parse(name, formdata, qdata, datatype, validation)
