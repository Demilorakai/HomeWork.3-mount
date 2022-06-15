import random

from aiogram import types, Dispatcher

from config import bot




#@dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith('pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)
    await bot.send_message(message.from_user.id, message.text)
    a = int(message.text)
    await bot.send_message(message.from_user.id, a**2)




def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)