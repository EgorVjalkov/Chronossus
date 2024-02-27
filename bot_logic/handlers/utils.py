from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from typing import Any
from bot_logic.handlers.available_variants import non_build_combos


def combo_is_build(list_of_exps, new_exp) -> bool:
    for exp in list_of_exps:
        if exp in non_build_combos:
            if new_exp in non_build_combos[exp]:
                return False
    return True


async def append_data_and_answer(callback: CallbackQuery,
                                 state: FSMContext,
                                 key: str,
                                 value: Any):
    data = await state.get_data()
    if key in data:
        if value in data[key]:
            await callback.answer(f"Already added!")
            return

        else:
            if combo_is_build(data[key], value):
                data[key].append(value)
            else:
                await callback.answer(f"Non build combo!")

    else:
        data[key] = [value]

    await state.update_data(data)
    await callback.answer(f"{value} added to {key}.")
    return


async def get_show_data(state: FSMContext) -> str:
    data = await state.get_data()
    if not data:
        return 'Create your build.'
    else:
        show_data = ['Your build: ']
        for k in data:
            match data[k]:
                case list():
                    show_data.append(
                        f"{k} -> {', '.join(data[k])}")
                case str():
                    show_data.append(
                        f"{k} -> {data[k]}")
        return '\n'.join(show_data)

