from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


def get_potion_type_keyboard():
    
    kb = [
        [KeyboardButton(text="Зелье"), KeyboardButton(text="Взрывное зелье")],
        [KeyboardButton(text="Оседающее зелье"), KeyboardButton(text="Стрела")]
    ]
    
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)