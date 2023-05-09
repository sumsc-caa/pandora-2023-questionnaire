from jinja2 import Template


class BaseComponent(object):
    '''表单组件的基类'''

    # jinja2模板，定义了组件的外观
    template = Template("""
        <div class="row">
            <div class="col-md-6 mb-3">
                <label>{{caption}}</label>
                <span id="{{name}}" class="text-warning">尚未实现的组件{{compname}}</span>
            </div>
        </div>
    """)
    
    def render(self, name: str, caption: str, **data: dict):
        """渲染组件的函数。所有子类都应该继承这个方法"""
        return self.template.render(
            compname = self.__class__.__name__,
            caption = caption,
            name = name,
            **data,
        )


components: dict[str, BaseComponent] = {}

def register_component(cls):
    components[cls.__name__] = cls()