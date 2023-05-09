from .BaseComponent import BaseComponent, Template, register_component

# 添加装饰器使程序能加载并注册这个组件
@register_component
class RadioSelect(BaseComponent):
    """单选框"""
    # TODO: 完善组件
    
    template = Template("")

    def render(self, name: str, caption: str, options: list[tuple[str, str]], placeholder: str = "", required = True, desc: str = "", **_):
        """单选框

        Args:
            name (str): 问卷项的名称
            caption (str): 问卷项标题（题干）
            option (list[(key: str, value: str)]): 可选项
                key (str): 该项的键（存入表单的值）
                value (str): 该项的展示值（渲染时展示的值）
            placeholder (str, optional): 输入提示. Defaults to "".
            required (bool, optional): 是否必须. Defaults to True.
            desc (str, optional): 字段描述. Defaults to "".

        Returns:
            str: 渲染好的问卷
        """
        return self.template.render()
