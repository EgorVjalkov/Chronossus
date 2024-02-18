from aiogram.fsm.state import StatesGroup, State

from bot_logic.handlers.available_variants import states_game_buildings


class BuildGame(StatesGroup):
    start_choosing = State()
    in_game = State()


class ChronossusCommand(StatesGroup):
    new_era_starting = State()
    choosing_first_player = State()
    applying_bot_command = State()
