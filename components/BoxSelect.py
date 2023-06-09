from werkzeug.datastructures import ImmutableMultiDict
from .BaseComponent import BaseComponent, Template, register_component, FormValueError

# 添加装饰器使程序能加载并注册这个组件


@register_component
class BoxSelect(BaseComponent):
    """多选框
    参考：https://getbootstrap.com/docs/5.2/forms/checks-radios/#checks
    """
    template = Template("""
        <div class="row">
            <div class="mb-3 checkbox-group"
                data-min="{{num_selections[0]}}"
                data-max="{{num_selections[1]}}"
            >
                <label for="{{name}}">{{index}}. {{caption}}</label>
                {% for option in options %}
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="{{name}}"
                            id="{{name}}_{{loop.index}}" value="{{option[0]}}"
                        >
                        <label class="form-check-label" for="{{name}}_{{loop.index}}">
                            {{option[1]}}
                        </label>
                    </div>
                {% endfor %}
                <div class="alert alert-danger fade show py-1"
                    role="alert" style="display:none; width:fit-content;">
                    请选择至少 {{num_selections[0]}} 项，至多 {{num_selections[1]}} 项
                </div>
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
               desc: str = "",
               num_selections: tuple[int, int] = (-1, -1),
               **_):
        """多选框

        Args:
            index (int): 问题序号
            name (str): 问题名称（存储时使用）
            caption (str): 问题题干
            options (list[(key: str, value: str)]): 问题的选项
                key (str): 该项的键（存入表单的值）
                value (str): 该项的展示值（渲染时展示的值）
            desc (str, optional): 字段描述. Defaults to "".
            num_selections (tuple[int, int], optional):
                最少选择 num_selections[0] 项，最多选择 num_selections[1] 项.
                Defaults to (1,len(options)).
        Returns:
            str: 渲染好的问卷
        """
        if num_selections[0] < 0:
            num_selections = (1, len(options))
        return self.template.render(
            index=index,
            name=name,
            caption=caption,
            options=options,
            desc=desc,
            num_selections=num_selections,
        )

    def parse(self,
              name: str,
              formdata: ImmutableMultiDict,
              qdata=None,
              datatype='str',
              validation=None):
        # 需要返回一个列表，里面是用户选中的所有项
        # 验证是否用户所选项都在问题提供的选项内
        selected = formdata.getlist(name)
        options = [option[0] for option in qdata['options']]
        for i in selected:
            if i not in options:
                raise FormValueError("Invalid option selected.")
        return selected
