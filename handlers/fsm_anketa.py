from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


from config import bot
from keyboards.client_kb import cancel_markup


class FSMAdmin(StatesGroup):
    photo = State()
    title = State()
    description = State()
    amount = State()
    region = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.photo.set()
        await message.answer(f"Здравствуйте {message.from_user.full_name}, "
                             f"Отправьте фото блюда...",
                             reply_markup=cancel_markup)
    else:
        await message.reply("Пишите в личный чат!")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Название блюда?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await FSMAdmin.next()
    await message.answer("Описание блюда?")


async def load_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("В каком количестве?")


async def load_age(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['amount'] = message.text
        await FSMAdmin.next()
        await message.answer("Местоположение?")
    except:
        await message.answer("Только числа!")


async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await bot.send_photo(message.from_user.id,
                             data['photo'],
                             caption=f"Title: {data['title']}\n"
                                     f"Description: {data['description']}\n"
                                     f"Amount: {data['amount']}\n"
                                     f"{data['username']}")
        print(data)

    await state.finish()
    await message.answer("Заказ принят)")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Регистрация отменена!")


def register_handler_fsmanketa(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*',
                                commands='cancel')
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(fsm_start, commands=['anketa'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.title)
    dp.register_message_handler(load_surname, state=FSMAdmin.title)
    dp.register_message_handler(load_age, state=FSMAdmin.amount)

