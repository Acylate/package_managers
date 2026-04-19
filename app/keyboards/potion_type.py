from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


def get_potion_type_keyboard():
    kb = [
        [InlineKeyboardButton(text="Зелье", callback_data="potion_regular")],
        [InlineKeyboardButton(text="Взрывное зелье", callback_data="potion_splash")],
        [InlineKeyboardButton(text="Оседающее зелье", callback_data="potion_lingering")],
        [InlineKeyboardButton(text="Стрела", callback_data="potion_arrow")]
    ]

    return InlineKeyboardMarkup(inline_keyboard=kb)