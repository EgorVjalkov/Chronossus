from aiogram.types import Message
from bot_logic.phases.basephase import BasePhase


class ParadoxPhase(BasePhase):
    need_roll_menu_vars = ('need', 'not need')
    roll_menu_vars = ('roll', 'back')
    available_vars = need_roll_menu_vars + roll_menu_vars

    def __init__(self):
        super().__init__('Paradox')

    def player_roll_menu(self, message: Message):
        self.answer = 'Do you need roll paradoxes?'
        self.vars = self.need_roll_menu_vars
        return self.get_phase_kb(message)

    def rolling_menu(self, message: Message):
        self.answer = 'Click '"roll"' if you need rolling'
        self.vars = self.roll_menu_vars
        return self.get_phase_kb(message)

    def roll_paradoxes_and_publish_result(self):
        pass
