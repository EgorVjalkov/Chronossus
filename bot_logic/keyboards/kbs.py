from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from bot_logic.handlers.available_variants import GameBuildCategory


def simple_kb(variants_list) -> ReplyKeyboardMarkup:
    keys = [KeyboardButton(text=i) for i in variants_list]
    return ReplyKeyboardMarkup(keyboard=[keys], resize_keyboard=True)


async def answer_as_simple_kb(message: Message,
                              answer: str,
                              variants_list: list) -> None:
    await message.answer(answer, reply_markup=simple_kb(variants_list))


def get_keyboard(keys_list, rows=None) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for key in keys_list:
        keyboard.add(KeyboardButton(text=key))
    if rows:
        keyboard.adjust(rows)
    else:
        keyboard.adjust(5)
    return keyboard.as_markup(resize_keyboard=True)


def get_filling_inline(category: GameBuildCategory, acc_keys: list) -> InlineKeyboardBuilder:
    # тут можно прикрутить перевод на инглишь

    state = category.category_name
    keys = category.buttons
    keys.extend(acc_keys)
    print(keys)

    inline = InlineKeyboardBuilder()
    keys = [InlineKeyboardButton(text=str(btn), callback_data=f'fill_{state}_{btn}')
            for btn in keys]

    max_in_row = 2
    if len(keys) % max_in_row > 0:
        groups = len(keys) // max_in_row + 1
    else:
        groups = len(keys) // max_in_row
    group_keys_list = []
    for i in range(1, groups+1):
        group_keys_list.append(keys[:max_in_row])
        keys = [i for i in keys if keys.index(i) >= max_in_row]

    for g in group_keys_list:
        inline.row(*g)
    return inline
