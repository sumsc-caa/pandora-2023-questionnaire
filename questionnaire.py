import json
from database import Database
from components import components


class Questionnaire:
    def __init__(self, qid: int, name: str, desc: str | None = None,
                 queries_json: str = "[]"):
        self.qid = qid
        self.name = name
        self.desc = desc or ""
        try:
            self.queries = json.loads(queries_json)
        except Exception as e:
            print(queries_json)
            raise e

    def __repr__(self) -> str:
        return f"<Questionnaire with qid={self.qid} name={self.name}>"

    def render(self):
        """渲染问卷"""
        parts = []
        for index, q in enumerate(self.queries, start=1):
            type = q["type"]
            component = components.get(type, None)
            if component is None:
                component = components["FallBack"]
                html = component.render(index, ogtype=type, **q)
            else:
                html = component.render(index, **q)
            parts.append(html)
        return ''.join(parts)

    def parse(self, formdata):
        """解析表单"""
        result = {}
        for q in self.queries:
            type = q["type"]
            component = components.get(type, None)
            key = q["name"]
            if component is None:
                value = None
            else:
                value = component.parse(key, formdata, q)
            result[key] = value
        return result

    @classmethod
    def get_questionnaire(cls, qid: int):
        """获取问卷"""
        with Database() as db:
            cur = db.execute(
                "SELECT * FROM questionnaire WHERE qid = ?", (qid,))
            result = cur.fetchone()
        if not result:  # result为空（问卷不存在）
            return None
        else:
            return cls(*result)


if __name__ == "__main__":
    q = Questionnaire(1, "test", queries_json='''[
        {"type":"InputBox", "name":"inputbox",
         "caption":"输入一些东西", "placeholder":"这是占位符"}
    ]''')
    print(q.render())
