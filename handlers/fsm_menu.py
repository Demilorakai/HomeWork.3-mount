from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import ADMIN
from config import bot
from database import bot_db
from keyboards.client_kb import cancel_markup

class FSMAdmin(StatesGroup):
    photo = State()
    title = State()
    description = State()
    price = State()
    col = State()


async def fsm_menu(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.answer("Ты не мой БОСС!!!")
    else:
        await FSMAdmin.photo.set()
        await message.answer(f"Здравствуйте {message.from_user.full_name}, "
                             f"Отправьте фото блюда...",
                             reply_markup=cancel_markup)



async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Название блюда?")

async def load_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await FSMAdmin.next()
    await message.answer("Описание блюда?")

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("Стоимость товара?")

async def load_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = message.text
        await FSMAdmin.next()
        await message.answer("Количество блюд?")
    except:
        await message.answer("Цена блюда не может быть отрицательной!")




async def load_count(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['col'] = message.text
        await bot.send_photo(message.from_user.id,
                             data['photo'],
                             caption=f"Title: {data['title']}\n"
                                     f"Description: {data['description']}\n"
                                     f"price: {data['price']}\n"
                                     f"{data['col']}")
        print(data)
    await bot_db.sql_command_insert(state)
    await state.finish()
    await message.answer("Заказ принят)")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Заказ отменен!")


def register_handler_menu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*',
                                commands='cancel')
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(fsm_menu, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_title, state=FSMAdmin.title)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(load_count, state=FSMAdmin.col)
