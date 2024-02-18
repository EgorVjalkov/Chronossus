
from bot_logic.My_token import TOKEN
import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot_logic.handlers import handlers


logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(handlers.start_building_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def bot_run():
    asyncio.run(main())


if __name__ == '__main__':
    bot_run()
