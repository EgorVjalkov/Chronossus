from aiogram.fsm.context import FSMContext
from aiogram.types import Message


def extract_callback_data(callback: str, keys: list) -> dict:
    string_list = callback.split('_')[1:]
    callback_dict = list(zip(keys, string_list))
    callback_dict = {i[0]: i[1] for i in callback_dict}
    return callback_dict


async def get_last_message(state: FSMContext) -> Message:
    data = await state.get_data()
    return data['last_message']



