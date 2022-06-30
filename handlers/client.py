import aiogram
from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot
from keyboards.client_kb import start_markup
from PARSERING import movies, multici, Anime


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello my master {message.from_user.full_name}",
                           reply_markup=start_markup)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1',
    )
    markup.add(button_call_1)

    question = 'Какой палец самый длинный?'
    answers = [
        'Большой', 'Указательный', 'Средний', 'Безымянный', 'Мизинец'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def mem (message: types.Message):
    photo = open('Photos/mem-2-1024x683.jpg', 'rb')
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
    await bot.send_message(message.chat.id,"Сколько тебе лет?",
                           reply_markup=markup)


async def serial(message: aiogram.types.Message):
    data = movies.parser_serials()
    for movie in data:
        desc = movie['desc'].split(', ')
        await bot.send_message(
            message.from_user.id,
            f"{movie['title']}\n"
            f"Год: {desc[0]}\n"
            f"Город: {desc[1]}\n"
            f"Жанр: #{desc[2]}\n\n"
            f"{movie['link']}"
        )


async def mult(message: aiogram.types.Message):
    data = multici.parser_mult()
    for movie in data:
        desc = movie['desc'].split(', ')
        await bot.send_message(
            message.from_user.id,
            f"{movie['title']}\n"
            f"Год: {desc[0]}\n"
            f"Город: {desc[1]}\n"
            f"Жанр: #{desc[2]}\n\n"
            f"{movie['link']}"
        )


async def anime(message: aiogram.types.Message):
    data = Anime.parser_animeshki()
    for movie in data:
        desc = movie['desc'].split(', ')
        await bot.send_message(
            message.from_user.id,
            f"{movie['title']}\n"
            f"Год: {desc[0]}\n"
            f"Город: {desc[1]}\n"
            f"Жанр: #{desc[2]}\n\n"
            f"{movie['link']}"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(callback, commands=['Q'])
    dp.register_message_handler(serial, commands=['serial'])
    dp.register_message_handler(mult, commands=['mult'])
    dp.register_message_handler(anime, commands=['anime'])
