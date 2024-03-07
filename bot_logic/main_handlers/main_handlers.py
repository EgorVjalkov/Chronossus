from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove


from bot_logic.keyboards.kbs import answer_as_kb
from bot_logic.dialogs.states import BuildGame
from bot_logic.main_handlers.available_variants import building_menu_vars


router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(BuildGame.building_menu)
    await message.answer('Hi, skin bastard.')
    await answer_as_kb(
        message,
        'I remind you, Creators don`t recommend including more then 2-3 expansions to base.',
        building_menu_vars)


@router.message(Command('abort'))
async def abort(message: Message, state: FSMContext) -> None:
    await message.answer('You abort a game. See you.',
                         reply_markup=ReplyKeyboardRemove())
    await state.clear()

