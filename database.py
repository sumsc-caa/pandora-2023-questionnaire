# built-in packages
import sqlite3
import contextlib

# ---------------------------------------------------------------------------- #
#                                database utils                                #
# ---------------------------------------------------------------------------- #

def Database(path = "db.sqlite3"):
    # 连接数据库（如果文件不存在会自动创建SQLite3数据库文件）
    # 比较理想的做法是单独开一个线程来处理与数据库的通信，这里为了降低难度就不这样做了
    db = sqlite3.connect(path)

    # 初始化
    # SQL语句在大二下学期数据库课程里会学到的
    ## 存储问卷数据
    db.execute("""
        CREATE TABLE IF NOT EXISTS questionnaire(
            qid INTEGER PRIMARY KEY ASC,
            name TEXT NOT NULL,
            desc TEXT,
            form TEXT NOT NULL
        )""")
    ## 存储收集到的问卷回答
    db.execute("""
        CREATE TABLE IF NOT EXISTS formvalue(
            id INTEGER PRIMARY KEY ASC,
            qid INTEGER,
            value TEXT NOT NULL
        )""")
    ### 创建索引加快查找速度
    db.execute("CREATE INDEX qid_id_formvalue on formvalue(qid, id);")

    # 在退出with语句块时自动关闭连接
    return contextlib.closing(db)

def Q(s):
    return f"%{s}%"
