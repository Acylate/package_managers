from aiogram import F
from aiogram.types import Message
from aiogram import Router

from app.keyboards.potion_type import get_potion_type_keyboard


router_start = Router()

@router_start.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я генератор зелий, я могу тебе помочь с созданием любого зелья, просто выбери парочку эффектов и я дам тебе команду!",
        reply_markup=get_potion_type_keyboard()
    )