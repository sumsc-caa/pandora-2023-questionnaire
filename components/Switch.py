from .BaseComponent import BaseComponent, Template, register_component
from .BaseComponent import ImmutableMultiDict

# 添加装饰器使程序能加载并注册这个组件


@register_component
class Switch(BaseComponent):
    """开关
    参考：https://getbootstrap.com/docs/5.2/forms/checks-radios/#switches
    """

    template = Template("""
        <div class="row">
            <div class="col mb-3">
                <label for="{{name}}">{{index}}. {{caption}}</label>
                <div class="form-switch">
                    <input name="{{name}}" class="form-check-input" type="checkbox"
                      role="switch" id="switch{{index}}"
                        {{isChecked}} {{isRequired}}>
                    <label class="form-check-label" for="switch{{index}}">
                    {{desc}}
                    </label>
                </div>
            </div>
        </div>""")

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


        check = "checked" if default else ""
        require = "reqeired" if required else ""

        return self.template.render(
            index=index,
            caption=caption,
            isChecked = check,
            isRequired = require,
            desc = desc,
            name=name
            )

    # ruff: noqa: F811

    def parse(self,
              name: str,
              formdata: ImmutableMultiDict,
              qdata=None,
              datatype='bool',
              validation=None):
        data = formdata.get(name, None)
        return bool(data)
