from aiogram import Bot
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from bot_logic.keyboards.kbs import answer_as_kb
from bot_logic.keyboards.inlines import get_filling_inline, GameBuildCallback
from bot_logic.handlers.states import BuildGame
from bot_logic.handlers.available_variants import GameBuildCategory, building_menu_vars
from bot_logic.handlers.utils import append_data_and_answer, get_show_data
from bot_logic.My_token import TOKEN

from chronossus.classes.chronossus import Chronossus


bot = Bot(TOKEN)
start_building_router = Router()


@start_building_router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(BuildGame.building_menu)
    await message.answer('Hi, skin bastard.')
    await answer_as_kb(
        message,
        'I remind you, Creators don`t recommend including more then 2-3 expansions to base.',
        building_menu_vars)


@start_building_router.message(BuildGame.building_menu, F.text.in_(building_menu_vars))
async def build_choosen(message: Message, state: FSMContext):

    if message.text == 'abort':
        await abort(message, state)

    elif message.text == 'start session':
        await init_chronossus(message, state)

    else:
        await message.answer('Apply', reply_markup=ReplyKeyboardRemove())
        category = GameBuildCategory(message.text)
        callback = get_filling_inline(category, ('back',))
        await message.answer(category.answer,
                             reply_markup=callback.as_markup())


async def abort(message: Message, state: FSMContext) -> None:
    await message.answer('You abort a game. See you.',
                         reply_markup=ReplyKeyboardRemove())
    await state.clear()


async def init_chronossus(message: Message, state: FSMContext) -> None:
    await message.answer('Game is starting.',
                         reply_markup=ReplyKeyboardRemove())
    game_build = await state.get_data()
    game_build = {i.replace(' ', '_'): game_build[i] for i in game_build}
    print('build', game_build)
    chron = Chronossus(**game_build)
    print(chron)
    await state.set_state(BuildGame.game)


game_building_router = Router()
start_building_router.include_router(game_building_router)


@start_building_router.callback_query(F.data.contains(GameBuildCallback.__prefix__))
async def fill_by_callback(callback: CallbackQuery, state: FSMContext) -> None:

    match tuple(GameBuildCallback.unpack(callback.data)):

        case [_, (_, variant), _] if variant == 'back':
            print(variant)
            await answer_as_kb((bot, callback.from_user.id),
                               await get_show_data(state),
                               building_menu_vars)

        case [(_, category), (_, variant), (_, add_flag)]:
            if add_flag:
                if variant == 'clear':
                    await state.set_data({category: []})
                    await callback.answer(f"Cleared.")

                else:
                    await append_data_and_answer(callback, state, category, variant)
            else:
                await state.update_data({category: variant})
                await callback.answer(f"{variant} is choosed as {category}.")
    # логи
    data = await state.get_data()
    print(data)

