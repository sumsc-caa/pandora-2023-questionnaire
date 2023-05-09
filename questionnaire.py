import json
from database import Database
from components import components


class Questionnaire:
    def __init__(self, qid: int, name: str, desc: str | None = None, queries_json: str = "[]"):
        self.qid = qid
        self.name = name
        self.desc = desc or ""
        self.queries = json.loads(queries_json)
    
    def __repr__(self) -> str:
        return f"<Questionnaire with qid={self.qid} name={self.name}>"
    
    def render(self):
        """渲染问卷"""
        parts = []
        for q in self.queries:
            type = q["type"]
            component = components.get(type, None)
            if component is None:
                component = components.get("FallBack")
            parts.append(component.render(**q))
        return ''.join(parts)
    

    @classmethod
    def get_questionnaire(cls, qid: int):
        """获取问卷"""
        with Database() as db:
            cur = db.execute("SELECT * FROM questionnaire WHERE qid = ?", (qid,))
            result = cur.fetchone()
        if not result: # result为空（问卷不存在）
            return None
        else:
            return cls(*result)

if __name__ == "__main__":
    q = Questionnaire(1, "test", queries_json='[{"type":"InputBox", "name":"inputbox", "caption":"输入一些东西"}]')
    print(q.render())