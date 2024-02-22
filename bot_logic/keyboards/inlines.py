from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from bot_logic.handlers.available_variants import GameBuildCategory
from bot_logic.keyboards.row_len_analyzer import RowLenAnalyzer


class GameBuildCallback(CallbackData, prefix='f.i.l.l'):
    category: str
    btn: str
    add_flag: bool


def get_filling_inline(category: GameBuildCategory, acc_keys: tuple = ()) -> InlineKeyboardBuilder:
    # тут можно прикрутить перевод на инглишь
    inline = InlineKeyboardBuilder()

    keys = list(category.buttons)
    keys.extend(acc_keys)
    flag = True if 'clear' in keys else False
    rows_list = RowLenAnalyzer(keys).create_row_container()

    for row in rows_list:
        cb_data_list = [GameBuildCallback(category=category.name, btn=k, add_flag=flag)
                        for k in row]
        callbacks = [InlineKeyboardButton(text=cb.btn, callback_data=cb.pack()) for cb in cb_data_list]
        inline.row(*callbacks)

    return inline


cat = GameBuildCategory('expansions')
get_filling_inline(cat, ('next', 'abort'))

