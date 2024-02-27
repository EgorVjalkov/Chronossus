from aiogram import Bot
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from typing import Tuple

from bot_logic.keyboards.row_len_analyzer import RowLenAnalyzer


def simple_kb(variants: tuple) -> ReplyKeyboardMarkup:

    keyboard = ReplyKeyboardBuilder()
    button_rows = RowLenAnalyzer(list(variants)).create_row_container()

    for row in button_rows:
        row = [KeyboardButton(text=k) for k in row]
        keyboard.row(*row)

    return keyboard.as_markup(resize_keyboard=True)


async def answer_as_kb(mod: Tuple | Message,
                       answer: str,
                       variants: tuple) -> None:
    match mod:
        case [bot, int(chat_id)] if isinstance(bot, Bot):
            await bot.send_message(chat_id, answer, reply_markup=simple_kb(variants))
        case Message():
            await mod.answer(answer, reply_markup=simple_kb(variants))

