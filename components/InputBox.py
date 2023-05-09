from .BaseComponent import BaseComponent, Template, register_component

# 添加装饰器使程序能加载并注册这个组件
@register_component
class InputBox(BaseComponent):
    """输入框（这是示例，别的组件可以仿照这个写）"""

    template = Template("""
        <div class="row">
            <div class="col-md-6 mb-3">
                <label for="{{name}}">{{caption}}</label>
                <input type="text" class="form-control" id="{{name}}" required="{{required}}" placeholder="{{placeholder}}">
                {% if desc %}<div id="inputHelp" class="form-text">{{desc}}</div>{% endif %}
            </div>
        </div>
    """)

    def render(self, name: str, caption: str, placeholder: str = "", required = True, desc: str = "", **_):
        """输入框

        Args:
            name (str): 问卷项的名称
            caption (str): 问卷项标题（题干）
            placeholder (str, optional): 输入提示. Defaults to "".
            required (bool, optional): 是否必须. Defaults to True.
            desc (str, optional): 字段描述. Defaults to "".

        Returns:
            str: 渲染好的问卷
        """
        return self.template.render(
            name = name,
            caption = caption,
            required = 'true' if required else 'false',
            placeholder = placeholder,
            desc = desc,
        )
