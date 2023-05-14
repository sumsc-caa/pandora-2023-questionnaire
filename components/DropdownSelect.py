from .BaseComponent import BaseComponent, Template, register_component, FormValueError
from .BaseComponent import ImmutableMultiDict

# 添加装饰器使程序能加载并注册这个组件


@register_component
class DropdownSelect(BaseComponent):
    """下拉选择框
    参考：https://getbootstrap.com/docs/5.2/forms/select/
    """
    template = Template("""
        <div class="row">
            <div class="col-md-6 mb-3">
                <label for="{{name}}">{{index}}. {{caption}}</label>
                <select class="form-select" id="{{name}}" name="{{name}}" required>
                    <option value="" selected disabled>{{placeholder}}</option>
                    {% for option in options %}
                        <option value="{{option[0]}}">{{option[1]}}</option>
                    {% endfor %}
                </select>
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
               placeholder: str = "",
               required=True,
               desc: str = "",
               **_):
        """
        Args:
            index (int): 问题序号
            name (str): 问题名称（存储时使用）
            caption (str): 问题题干
            options (list[(key: str, value: str)]): 问题的选项
                key (str): 该项的键（存入表单的值）
                value (str): 该项的展示值（渲染时展示的值）
            placeholder (str, optional): 输入提示. Defaults to "".
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
            placeholder=placeholder,
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
