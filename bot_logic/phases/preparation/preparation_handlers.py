from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot_logic.phases.states import PreparationPhase, ParadoxPhaseStates, PowerUpPhase
from bot_logic.phases.paradox.logic import ParadoxPhase
from bot_logic.phases.basephase import BasePhase


router = Router()


@router.message(PreparationPhase, F.text == 'next')
async def preparation_phase(message: Message,
                            state: FSMContext) -> None:

    await state.set_state(ParadoxPhaseStates.paradox_menu)
    await ParadoxPhase().player_roll_menu(message)
    #data = await state.get_data()
    #era_num = data['Chronossus'].chronology_track.value
    #if era_num == 1:
    #    await state.set_state(PowerUpPhase)
    #    await BasePhase('Power up').get_phase_kb(message)
    #else:
    #    await state.set_state(ParadoxPhaseStates.paradox_menu)
    #    await ParadoxPhase().player_roll_menu(message)
