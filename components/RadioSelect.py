from .BaseComponent import BaseComponent, Template, register_component, FormValueError
from .BaseComponent import ImmutableMultiDict

# 添加装饰器使程序能加载并注册这个组件


@register_component
class RadioSelect(BaseComponent):
    """单选框"""
    # TODO: 完善组件

    template = Template("""
        <div class="row">
            <div class="mb-3 radio-group">
                <label>{{index}}. {{caption}}</label>
                {% for option in options %}
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="{{name}}"
                            id="{{name}}_{{loop.index}}" value="{{option[0]}}" required>
                        <label class="form-check-label" for="{{name}}_{{loop.index}}">
                            {{option[1]}}
                        </label>
                    </div>
                {% endfor %}
                {% if desc %}
                    <div id="{{name}}-help" class="form-text">{{desc}}</div>
                {% endif %}
            </div>
        </div>
    """)

    def render(self,
               index: int,
               name: str,
               caption: str,
               options: list[tuple[str, str]],
               required=True,
               desc: str = "",
               **_):
        """单选框
        参考：https://getbootstrap.com/docs/5.2/forms/checks-radios/#radios

        Args:
            index (int): 问题序号
            name (str): 问题名称（存储时使用）
            caption (str): 问题题干
            option (list[(key: str, value: str)]): 问题的选项
                key (str): 该项的键（存入表单的值）
                value (str): 该项的展示值（渲染时展示的值）
            required (bool, optional): 是否必须. Defaults to True.
            desc (str, optional): 字段描述. Defaults to "".

        Returns:
            str: 渲染好的问卷
        """
        return self.template.render(
            index=index,
            name=name,
            caption=caption,
            options=options,
            required='true' if required else 'false',
            desc=desc,
        )

    def parse(self,
              name: str,
              formdata: ImmutableMultiDict,
              qdata=None,
              datatype='str',
              validation=None):
        # 验证是否用户所选都在问题提供的选项内
        selected = formdata.get(name)
        options = [option[0] for option in qdata['options']]
        if selected not in options:
            raise FormValueError("Invalid option selected.")

        return selected
