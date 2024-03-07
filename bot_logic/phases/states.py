from aiogram.fsm.state import StatesGroup, State


PreparationPhase = State()


class ParadoxPhaseStates(StatesGroup):
    paradox_menu = State()
    player_roll_menu = State()
    chronossus_roll_menu = State()


PowerUpPhase = State()


