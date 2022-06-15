from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot

async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello my master {message.from_user.id}")


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1',
    )
    markup.add(button_call_1)

    question = 'Чему равно число пи?'
    answers = [
        '3.15', '4.35', '3.14', '3.13'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )
async def mem (message: types.Message):
    photo = open('Photos/mem-2-1024x683.jpg','rb')
    await bot.send_photo(message.chat.id, photo=photo)

async def callback (message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton(
        "Меньше 18ти",
        callback_data='button_call_5',
    )
    button_call_6 = InlineKeyboardButton(
        "Больше 18ти",
        callback_data='button_call_6',
    )
    markup.add(button_call_5,button_call_6)
    await bot.send_message(message.from_user.id,"Сколько тебе лет?",
                           reply_markup=markup)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(callback, commands=['Q'])