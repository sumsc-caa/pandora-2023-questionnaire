from .BaseComponent import BaseComponent, Template, register_component
from .BaseComponent import FormValueError, ImmutableMultiDict

# 添加装饰器使程序能加载并注册这个组件


@register_component
class InputBox(BaseComponent):
    """输入框
    参照：https://getbootstrap.com/docs/5.2/forms/overview/#form-text
    """
    # * 这是示例，别的组件可以仿照这个写

    template = Template("""
        <div class="row">
            <div class="col-md-6 mb-3">
                <label for="{{name}}">{{index}}. {{caption}}</label>
                <input type="text" name="{{name}}" class="form-control" id="{{name}}"
                    required="{{required}}" placeholder="{{placeholder}}"
                    value="{{value}}">
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
               placeholder: str = "",
               default="",
               required=True,
               desc: str = "",
               **_):
        """输入框

        Args:
            index (int): 问题序号
            name (str): 问题的名称
            caption (str): 问题题干
            placeholder (str, optional): 输入提示. Defaults to "".
            default (str, optional): 默认值
            required (bool, optional): 是否必须. Defaults to True.
            desc (str, optional): 字段描述. Defaults to "".

        Returns:
            str: 渲染好的问卷
        """
        return self.template.render(
            index=index,
            name=name,
            caption=caption,
            value=default,
            required='true' if required else 'false',
            placeholder=placeholder,
            desc=desc,
        )

    def parse(self,
              name: str,
              formdata: ImmutableMultiDict,
              qdata=None,
              datatype='str',
              validation=None):
        """解析表单，参见BaseComponent"""
        result = formdata.get(name, "")
        if datatype == "str":
            pass
        elif datatype == "int":
            result = int(result)
        elif datatype == "float":
            result = float(result)
        else:
            # 出现问题的时候 raise FormValueError
            raise FormValueError("Unsupported datatype")

        return result
