from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.client.session.aiohttp import AiohttpSession

from app.core.config import Config


async def set_commands():
    commands = [BotCommand(command='start', description='Start')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

session = AiohttpSession(proxy=f"http://{Config.PROXY_USER}:{Config.PROXY_PASSWORD}@{Config.PROXY_HOST}:{Config.PROXY_PORT}")
bot = Bot(token=Config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


#pfp bot (BotFather), description (BotFather), just some touches to the text (code)