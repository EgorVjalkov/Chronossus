from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot_logic.phases.paradox.logic import ParadoxPhase
from bot_logic.phases.states import ParadoxPhaseStates


router = Router()


@router.message(ParadoxPhaseStates.paradox_menu,
                F.text.in_(ParadoxPhase.need_roll_menu_vars))
async def paradox_main(message: Message,
                       state: FSMContext) -> None:

    paradox = ParadoxPhase()
    if message.text == 'need':
        await state.set_state(ParadoxPhaseStates.player_roll_menu)
        await paradox.rolling_menu(message)

    elif message.text == 'no need':
        await state.set_state(ParadoxPhaseStates.chronossus_roll_menu)
        pass # chronossus rolls, while get anomaly


@router.message(ParadoxPhaseStates.player_roll_menu,
                F.text.in_(ParadoxPhase.roll_menu_vars))
async def paradox_phase(message: Message,
                        state: FSMContext) -> None:

    paradox = ParadoxPhase()
    if message.text == 'roll':
        pass # roll paradox dice and await vars

    elif message.text == 'back':
        await state.set_state(ParadoxPhaseStates.paradox_menu)
        await paradox.player_roll_menu(message)

