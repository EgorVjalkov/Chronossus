from abc import ABC

import pandas as pd
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.context import FSMContext

from bot_logic.handlers.available_variants import building_menu_vars


class BuildGame(StatesGroup):
    building_menu = State()
    game = State()


class ChronossusCommand(StatesGroup):
    new_era_starting = State()
    choosing_first_player = State()
    applying_bot_command = State()
