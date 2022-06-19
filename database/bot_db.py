import sqlite3
from config import bot
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot_D.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS menu "
               "(photo TEXT,title TEXT, description TEXT,price INTEGER,col INTEGER)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO menu VALUES "
                       "(?,?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM menu").fetchall()
    random_user = random.choice(result)
    await bot.send_photo(
        message.from_user.id,
        photo=random_user[0],
        caption=f"title: {random_user[1]}\n"
                f"Description: {random_user[2]}\n"
                f"Price: {random_user[3]}\n"
                f"COL: {random_user[4]}\n"


    )


async def sql_command_all():
    return cursor.execute("SELECT * FROM menu").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM menu WHERE id == ?", (id, ))
    db.commit()


async def sql_commands_get_all_id():
    return cursor.execute("SELECT id FROM menu").fetchall()