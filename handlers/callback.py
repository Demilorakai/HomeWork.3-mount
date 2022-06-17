from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_2',
    )
    markup.add(button_call_2)

    question = 'Какой цвет глаз самый распространённый?'
    answers = [
        "Карий",
        "Зелёный",
        "Голубой",
        "Фиолетовый",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = 'ОТВЕЧАЙ!!!!'
    answers = [
        '4',
        '8',
        '4, 6',
        '2, 4',
        '5',
    ]
    photo = open('media/problem1.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

async def callback_1 (call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,"Миллениал")

async def callback_2 (call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_7 = InlineKeyboardButton(
        "Тайланд 🇹🇭",
        callback_data='button_call_7',
    )
    button_call_8 = InlineKeyboardButton(
        "Швеция 🇸🇪",
        callback_data='button_call_8',
    )
    markup.add(button_call_7, button_call_8)
    await bot.send_message(call.message.chat.id, "Ты можешь улететь за границу, куда полетишь?",
                           reply_markup=markup)

async def callback_3 (call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,"Ты в Тайланде!")

async def callback_4 (call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,"Ты в Щвеции!")

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(callback_1, lambda call: call.data == "button_call_5")
    dp.register_callback_query_handler(callback_2, lambda call: call.data == "button_call_6")
    dp.register_callback_query_handler(callback_3, lambda call: call.data == "button_call_7")
    dp.register_callback_query_handler(callback_4, lambda call: call.data == "button_call_8")