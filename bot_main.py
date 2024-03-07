import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot_logic.My_token import TOKEN
from bot_logic.main_handlers import main_handlers, build_menu_handlers
from bot_logic.phases.era_router import era_router

logging.basicConfig(level=logging.INFO)


async def main():
    storage = MemoryStorage()
    bot = Bot(TOKEN)
    dp = Dispatcher(storage=storage)
    dp.include_router(main_handlers.router)
    dp.include_router(build_menu_handlers.router)
    dp.include_router(era_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def bot_run():
    asyncio.run(main())


if __name__ == '__main__':
    bot_run()
