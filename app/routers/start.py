import sys

from aiogram import F
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.keyboards.potion_type import get_potion_type_keyboard
from app.keyboards.potion_effects import get_potion_effects_keyboard, get_more_potion_effects_keyboard
from app.potiongen.potion_generator import PotionGenerator


class PotionFSM(StatesGroup):
    selecting_effect = State()
    input_level = State()
    input_duration = State()
    ask_more_effects = State()


class NumberInRange(BaseFilter):
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value
        
    async def __call__(self, message: Message) -> bool:
        try:
            number = int(message.text)
            return self.min_value <= number <= self.max_value
        except ValueError:
            return False
            


router_start = Router()

@router_start.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        "Привет!👋\n Я генератор зелий! Я могу тебе помочь с созданием любого зелья 🧪, просто выбери парочку эффектов и я дам тебе команду!",
        reply_markup=get_potion_type_keyboard()
    )

@router_start.callback_query(F.data.startswith("potion_"))
async def handle_potion_type(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    potion_type = callback.data
    
    await state.update_data(potion_type=potion_type, effects=[])
    
    await callback.message.edit_text(
        "Отлично! Теперь выберите ✨эффект✨ для зелья:",
        reply_markup=get_potion_effects_keyboard()
    )
    
    await state.set_state(PotionFSM.selecting_effect)
    await callback.answer()
    
    
@router_start.callback_query(PotionFSM.selecting_effect, F.data.startswith("effect_"))
async def handle_effect_selection(callback: CallbackQuery, state: FSMContext):
    effect_name = callback.data.replace("effect_", "")
    await state.update_data(current_effect=effect_name)
    
    await callback.message.edit_text(
        f"Вы выбрали эффект: `{effect_name}`. \n\nВведите уровень📈 зелья (число):"
    )
    
    await state.set_state(PotionFSM.input_level)
    await callback.answer()
    
@router_start.message(PotionFSM.input_level, NumberInRange(1, 128))
async def handle_level_input(message:Message, state:FSMContext):
    level = int(message.text)
    await state.update_data(current_level=level)
    
    await message.answer("Введите длительность зелья ⏰(в секундах, -1 для бесконечного зелья):")
    await state.set_state(PotionFSM.input_duration)
    
@router_start.message(PotionFSM.input_level)
async def handle_invalid_level(message:Message):
    await message.answer("Пожалуйста❗ отправьте число (от 1 до 128) для уровня зелья.")
    
@router_start.message(PotionFSM.input_duration, NumberInRange(-1, sys.maxsize))
async def handle_duration_input(message: Message, state: FSMContext):
    duration = int(message.text)
    
    data = await state.get_data()
    effects = data.get("effects", [])
    
    effects.append({
        "effect_name": data.get("current_effect"),
        "effect_level": data.get("current_level"),
        "effect_duration": duration
    })
    
    await state.update_data(effects=effects, current_effect=None, current_level=None)
    
    await message.answer(
        "Эффект сохранен!\nХотите добавить еще один эффект? 🤔",
        reply_markup=get_more_potion_effects_keyboard()
    )
    await state.set_state(PotionFSM.ask_more_effects)
    
@router_start.message(PotionFSM.input_duration)
async def handle_invalid_duration(message:Message):
    await message.answer("Пожалуйста❗ отправьте число (от -1) для длительности зелья.")
    
@router_start.callback_query(PotionFSM.ask_more_effects, F.data.in_(["add_effect", "finish"]))
async def handle_more_potion_effects(callback: CallbackQuery, state:FSMContext):
    if callback.data == "add_effect":
        await callback.message.edit_text(
            "Выберите следующий эффект✨:",
            reply_markup=get_potion_effects_keyboard()
        )
        await state.set_state(PotionFSM.selecting_effect)
    else:
        data = await state.get_data()
        potion_type = data.get("potion_type")
        effects = data.get("effects", [])
  
        # Генерация команды      
        pg = PotionGenerator()
        command = pg.generate_command(potion_type, effects)
        
        await callback.message.edit_text(
            f"Зелье готово!\nВот ваша команда 😊: <code>{command}</code>"
        )
        await state.clear()
    
    await callback.answer()