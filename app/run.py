import logging
import asyncio

from app.create import dp, bot
from app.core.config import Config
from app.routers.start import router_start


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def main():
    print(Config.PROXY_PASSWORD)
    dp.include_router(router_start)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
    