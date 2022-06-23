import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="Got your id!")


async def just_do_it():
    await bot.send_message(chat_id=chat_id, text="Пора спать!")


async def lets_play():
    media = open("media/b65327c0718351690a80fb07f974789a.jpg", "rb")
    await bot.send_photo(chat_id=chat_id, media=media, caption="ВСТАВААААЙ!!!!")


async def scheduler():
    aioschedule.every().thursday.at("14:59").do(just_do_it)
    aioschedule.every().wednesday.at("18:01").do(lets_play)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'Пора!' in word.text)


def sheduler():
    return None