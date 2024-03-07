from aiogram.fsm.state import StatesGroup, State

from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button

from bot_logic.main_handlers.available_variants import building_menu_vars


class BuildGame(StatesGroup):
    main_menu = State()
    building_menu = State()


main_window = Window(
    Const('Hi, skin bastard.'),
    Button(Const)


)


class Era(StatesGroup):

    preparation_phase = State()
    paradox_phase = State()
    power_up_phase = State()
    warp_phase = State()
    action_rounds_phase = State()
    clean_up_phase = State()

