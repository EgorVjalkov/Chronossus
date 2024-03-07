from aiogram import Router
from bot_logic.phases.preparation import preparation_handlers
from bot_logic.phases.paradox import paradox_handlers


era_router = Router()
era_router.include_routers(preparation_handlers.router,
                           paradox_handlers.router)
