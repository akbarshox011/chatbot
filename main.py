from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os

from keybords import generate_main_menu_button, back_button
from openwather import getweatherinfo
from getpicture import getrandompicture
from convertvalut import getconvertvalut


class Openweather(StatesGroup):
    city = State()


class Convertvalut(StatesGroup):
    fromvalstate = State()
    tovalstate = State()
    amountstate = State()


load_dotenv()
storage = MemoryStorage()
bot = Bot(os.getenv('telegramtoken'))

dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands='start')
async def start(message: Message):
    fullname = message.from_user.full_name
    chat_id = message.chat.id

    await bot.send_message(chat_id, f'Xush kelibsiz {fullname}!', reply_markup=generate_main_menu_button())


@dp.message_handler(text='⛅️ Ob-havo')
async def setopenweather(message: Message):
    await message.answer('Shahar nomini kiriting: ', reply_markup=back_button())
    await Openweather.city.set()


@dp.message_handler(state=Openweather.city)
async def getcityinfo(message: Message, state: FSMContext):
    city = message.text
    if city == '⬅️ Orqaga' or city == '/start':
        await state.finish()
        await message.answer('Kategoriyani tanlang', reply_markup=generate_main_menu_button())
    else:
        info = getweatherinfo(city)
        if len(info) == 2:
            info, image = info
            await message.answer_photo(photo=image, caption=info)
        else:
            await message.answer(info)


@dp.message_handler(text='🖼️ Rasmlar')
async def setopenweather(message: Message):
    image = getrandompicture()
    await message.answer_photo(photo=image)


@dp.message_handler(text='💰 Valyuta ayirboshlash')
async def convertvalut(message: Message):
    await message.answer('Qaysi valutadan: ', reply_markup=back_button())
    await Convertvalut.fromvalstate.set()


@dp.message_handler(state=Convertvalut.fromvalstate)
async def getfrom(message: Message, state: FSMContext):
    if message.text == '⬅️ Orqaga' or message.text == '/start':
        await message.answer('Bosh menu', reply_markup=generate_main_menu_button())
        await state.finish()
    else:
        await message.answer('Qaysi valutaga: ')
        await state.update_data({'fromval': message.text})
        await Convertvalut.tovalstate.set()


@dp.message_handler(state=Convertvalut.tovalstate)
async def getto(message: Message, state: FSMContext):
    if message.text == '⬅️ Orqaga' or message.text == '/start':
        await message.answer('Bosh menu', reply_markup=generate_main_menu_button())
        await state.finish()
    else:
        await message.answer('Summani kiriting:')
        await state.update_data({'toval': message.text})
        await Convertvalut.amountstate.set()


@dp.message_handler(state=Convertvalut.amountstate)
async def getamount(message: Message, state: FSMContext):
    if message.text == '⬅️ Orqaga' or message.text == '/start':
        await message.answer('Bosh menu', reply_markup=generate_main_menu_button())
        await state.finish()
    else:
        await state.update_data({'amount': message.text})
        data = await state.get_data()
        f = data['fromval']
        t = data['toval']
        a = data['amount']

        result = getconvertvalut(f, t, a)
        valut = result['result']
        text = f'Qaysi valutadan: {f}\n' \
               f'Qaysi valutaga: {t}\n' \
               f'Qiymat: {a} {f}\n' \
               f'Natija: {valut} {t}'
        await message.answer(text, reply_markup=generate_main_menu_button())
        await state.finish()


executor.start_polling(dp, skip_updates=True)
