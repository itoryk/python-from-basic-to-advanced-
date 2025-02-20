import sqlite3 as sq

db = sq.connect('tg.db')
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "tg_id INTEGER, "
                "name TEXT)")

    db.commit()


async def add_info(user_id, name_city):
    cur.execute(
        "INSERT INTO accounts (tg_id,name) VALUES (?,?)", (user_id, name_city)
    )

    db.commit()


async def get_list(user_id):
    return cur.execute("SELECT name FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchall()






