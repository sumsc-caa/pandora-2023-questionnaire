from jinja2 import Template
from werkzeug.datastructures import ImmutableMultiDict

components = {}


def register_component(cls):
    components[cls.__name__] = cls()
    return cls


class FormValueError(BaseException):
    def __init__(self, message: str, *args: object) -> None:
        super().__init__(*args)
        self.message = message


@register_component
class BaseComponent(object):
    '''表单组件的基类'''

    # jinja2模板，定义了组件的外观
    template = Template("""
        <div class="row">
            <div class="col mb-3">
                <label for="{{name}}">{{index}}. {{caption}}</label>
                <div class="ms-3">尚未实现的组件 <code>{{ogtype}}</code></div>
                <div class="ms-3">组件参数：
                    <code>{{args}}</code> <code>{{kwargs}}</code>
                </div>
            </div>
        </div>
    """)

    def render(self, index: int, name: str, caption: str, *args, **kwargs):
        """渲染组件的函数。所有子类都应该继承这个方法

        Args:
            index (int): 问题序号
            name (str): 问题名字
            caption (str): 问题题干

        Returns:
            str: 渲染后的html
        """
        return BaseComponent.template.render(
            index=index,
            caption=caption,
            ogtype=self.__class__.__name__,
            name=name,
            args=args,
            kwargs=kwargs,
        )

    def parse(
            self,
            name: str,
            formdata: ImmutableMultiDict,
            qdata=None,
            datatype='str',
            validation=None):
        """解析整理表单内容，返回可序列化的对象。所有子类都应该继承这个方法

        Args:
            name (str): 问题名字
            formdata (ImmutableMultiDict): 表单数据
            qdata (Any): 问题的数据
            datatype (str, optional): 数据类型. Defaults to 'str'.
            validation (list, optional): 表单验证（暂时不管）. Defaults to None.
        """

        raise NotImplementedError("该方法尚未实现")
