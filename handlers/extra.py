from aiogram import types, Dispatcher

from config import bot


async def echo(message: types.Message):
    x = message.text
    try:
        x = int(x)
        c = 1
    except:
        pass
        c = 0
    if c == 1:
        await bot.send_message(message.chat.id,f'{x*x}')
    elif c == 0:
        await bot.send_message(message.chat.id, x)
    else:
        pass


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
