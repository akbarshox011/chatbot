from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup


def generate_main_menu_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='⛅️ Ob-havo'),
        KeyboardButton(text='💰 Valyuta ayirboshlash'),
        KeyboardButton(text='🖼️ Rasmlar'),
        KeyboardButton(text='☑️ So\'rovnoma')
    )

    return markup




def back_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='⬅️ Orqaga'),

    )

    return markup