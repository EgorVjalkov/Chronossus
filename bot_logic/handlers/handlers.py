from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from bot_logic.keyboards.kbs import get_filling_inline, answer_as_simple_kb
from bot_logic.handlers.states import BuildGame
from bot_logic.handlers.available_variants import GameBuildCategory, states_game_buildings, game_build_dict
from bot_logic.handlers.utils import extract_callback_data, get_last_message

from chronossus.chronossus import Chronossus


start_building_router = Router()


@start_building_router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(BuildGame.start_choosing)
    await message.answer('Hi, skin bastard.')
    await answer_as_simple_kb(message,
                              'Choose your destiny.',
                              states_game_buildings)


@start_building_router.message(BuildGame.start_choosing, F.text.in_(states_game_buildings))
async def build_choosen(message: Message, state: FSMContext):
    await message.reply('Apply.', reply_markup=ReplyKeyboardRemove())
    category = GameBuildCategory(message.text)
    callback = get_filling_inline(category, ['next', 'abort', 'start a game'])
    await message.answer(category.answer,
                         reply_markup=callback.as_markup())
    await state.update_data(last_message=message)


game_building_router = Router()
start_building_router.include_router(game_building_router)


# тут нужно еще прикрутуть выбор нескольких вариантов


async def abort(message: Message, state: FSMContext) -> None:
    await message.answer('You abort a game. See you.')
    await state.clear()


async def init_chronossus(message: Message, state: FSMContext) -> None:
    await message.answer('Game is starting.')
    game_build = await state.get_data()
    game_build = {i.replace(' ', '_'): game_build[i]
                  for i in game_build if i != 'last_message'}
    print('build', game_build)
    chron = Chronossus(**game_build)
    print(chron)


@start_building_router.callback_query(F.data.contains('fill_'))
async def fill_by_callback(callback: CallbackQuery, state: FSMContext):

    last_message = await get_last_message(state)

    callback_data_dict = extract_callback_data(callback.data, ['category', 'variant'])
    category = callback_data_dict['category']
    variant = callback_data_dict['variant']
    print(variant)

    if variant == 'next':
        await answer_as_simple_kb(last_message,
                                  'Continue',
                                  states_game_buildings)
    elif variant == 'start a game':
        await init_chronossus(last_message, state)

    elif variant == 'abort':
        await abort(last_message, state)

    else:
        await state.update_data({category: variant})
        await callback.answer(f"{variant} is choosed as {category}.")
    # логи
        data = await state.get_data()
        del data['last_message']
        print(data)



