from bot_logic.keyboards.kbs import answer_as_kb
from aiogram.types import Message


class BasePhase:
    def __init__(self,
                 phase_name: str):
        self.phase_name = phase_name + ' phase'
        self.finish_button = 'next'
        self.default_variants = (self.finish_button,)
        self.phase_menu_answer = f'Click "{self.finish_button}" if you finished {self.phase_name}'

    @property
    def answer(self):
        return self.phase_menu_answer

    @answer.setter
    def answer(self, answer: str):
        self.phase_menu_answer = answer

    @property
    def vars(self):
        return self.default_variants

    @vars.setter
    def vars(self, variants: tuple):
        self.default_variants = variants

    async def get_phase_kb(self,
                           message: Message) -> None:
        await answer_as_kb(message,
                           self.answer,
                           self.vars)


class FirstPhase(BasePhase):
    def __init__(self, era_name):
        super().__init__(phase_name='preparation')
        self.era_name = era_name

        answer = [f'A {self.era_name} Era begins!',
                  f'Click "{self.finish_button}" if you finished {self.phase_name}']
        self.phase_menu_answer = '\n'.join(answer)

