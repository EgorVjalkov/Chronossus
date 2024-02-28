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
    def __init__(self, num_of_EXOs):
        self.num_of_EXOs = num_of_EXOs

        choosing_first_player = State()
        applying_bot_command = State()


