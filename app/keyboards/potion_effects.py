from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


def get_potion_effects_keyboard():
    kb = [
        [InlineKeyboardButton(text="speed", callback_data="effect_speed"), InlineKeyboardButton(text="slowness", callback_data="effect_slowness"), InlineKeyboardButton(text="haste", callback_data="effect_haste")],
        [InlineKeyboardButton(text="mining fatigue", callback_data="effect_mining fatigue"), InlineKeyboardButton(text="strength", callback_data="effect_strength"), InlineKeyboardButton(text="instant health", callback_data="effect_instant health")],
        [InlineKeyboardButton(text="instant damage", callback_data="effect_instant damage"), InlineKeyboardButton(text="jump boost", callback_data="effect_jump boost"), InlineKeyboardButton(text="nausea", callback_data="effect_nausea")],
        [InlineKeyboardButton(text="regeneration", callback_data="effect_regeneration"), InlineKeyboardButton(text="resistance", callback_data="effect_resistance"), InlineKeyboardButton(text="fire resistance", callback_data="effect_fire resistance")],
        [InlineKeyboardButton(text="water breathing", callback_data="effect_water breathing"), InlineKeyboardButton(text="invisibility", callback_data="effect_invisibility"), InlineKeyboardButton(text="blindness", callback_data="effect_blindness")],
        [InlineKeyboardButton(text="night vision", callback_data="effect_night vision"), InlineKeyboardButton(text="night vision", callback_data="effect_night vision"), InlineKeyboardButton(text="hunger", callback_data="effect_hunger")],
        [InlineKeyboardButton(text="weakness", callback_data="effect_weakness"), InlineKeyboardButton(text="poison", callback_data="effect_poison"), InlineKeyboardButton(text="wither", callback_data="effect_wither")],
        [InlineKeyboardButton(text="health boost", callback_data="effect_health boost"), InlineKeyboardButton(text="absorption", callback_data="effect_absorption"), InlineKeyboardButton(text="saturation", callback_data="effect_saturation")],
        [InlineKeyboardButton(text="glowing", callback_data="effect_glowing"), InlineKeyboardButton(text="levitation", callback_data="effect_levitation"), InlineKeyboardButton(text="luck", callback_data="effect_luck")],
        [InlineKeyboardButton(text="bad luck", callback_data="effect_bad luck"), InlineKeyboardButton(text="slow falling", callback_data="effect_slow falling"), InlineKeyboardButton(text="conduit power", callback_data="effect_conduit power")],
        [InlineKeyboardButton(text="dolphin's grace", callback_data="effect_dolphin's grace"), InlineKeyboardButton(text="bad omen", callback_data="effect_bad omen"), InlineKeyboardButton(text="hero of the village", callback_data="effect_hero of the village")],
        [InlineKeyboardButton(text="darkness", callback_data="effect_darkness")]
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_more_potion_effects_keyboard():
    kb = [
        [InlineKeyboardButton(text="Добавить еще эффект", callback_data="add_effect")],
        [InlineKeyboardButton(text="Завершить создание", callback_data="finish")]
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=kb)