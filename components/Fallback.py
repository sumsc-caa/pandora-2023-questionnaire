from .BaseComponent import BaseComponent, Template, register_component
from .BaseComponent import ImmutableMultiDict


@register_component
class FallBack(BaseComponent):
    '''不存在的组件'''

    # jinja2模板，定义了组件的外观
    template = Template("""
        <div class="row">
            <div class="col mb-3">
                <label for="{{name}}">{{index}}. {{caption}}</label>
                <div class="ms-3">不存在的组件 <code>{{ogtype}}</code></div>
                <div class="ms-3">组件参数：
                    <code>{{args}}</code> <code>{{kwargs}}</code></div>
            </div>
        </div>
    """)

    def render(self,
               index: int,
               name: str,
               caption: str,
               ogtype: str,
               *args,
               **kwargs):
        return self.template.render(
            index=index,
            caption=caption,
            ogtype=ogtype,
            name=name,
            args=args,
            kwargs=kwargs,
        )

    def parse(self,
              name: str,
              formdata: ImmutableMultiDict,
              qdata=None,
              datatype='str',
              validation=None):
        return None
