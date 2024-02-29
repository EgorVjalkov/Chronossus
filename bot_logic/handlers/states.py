from abc import ABC

import pandas as pd
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.context import FSMContext

from bot_logic.handlers.available_variants import building_menu_vars


class BuildGame(StatesGroup):
    building_menu = State()
    game = State()


class Era(StatesGroup):
    preparation_phase = State()
    paradox_phase = State()
    power_up_phase = State()
    warp_phase = State()
    action_rounds_phase = State()
    clean_up_phase = State()





