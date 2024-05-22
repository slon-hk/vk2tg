from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, FSInputFile
from aiogram.filters.command import Command
from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
import asyncio


import keyboard as kb
import db

bot = Bot(token="")
router = Router()
storage = MemoryStorage()
user_dict: dict[int, dict[str, str | int | bool]] = {}

class FSMFillForm(StatesGroup):
    reg = State()
    fill_token = State()
    fill_msg = State()
    await_comm = State()
    yes_no = State()

#Start message and registration

@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Привет Это бот Vk2Tg, он позволяет тебе общаться с твоими друзьями в Вк не уходя из телеграмма")
    db.db_start()
    await state.set_state(FSMFillForm.reg)
    # await registration(pass, pass)


@router.message(StateFilter(FSMFillForm.reg))
async def registration(message: types.Message, state: FSMContext):
    message.answer(text='filter')
    if db.filtr_db(message.from_user.id) == False:
        await message.answer(text='Введите токен')
        await state.set_state(FSMFillForm.fill_token)
    elif db.filtr_db(message.from_user.id) == True:
        await message.answer(text='Вы уже зарегестрированны.\nХотите изменить токен?', reply_markup=kb.yes_main)
        await state.clear()

@router.callback_query(F.data.in_('yes'),  StateFilter(default_state))
async def process_buttons_press(callback: CallbackQuery, state: FSMContext):
    if callback.message.text != 'Yes':
        await state.set_state(FSMFillForm.reg)
    await callback.answer()

@router.callback_query(F.data.in_('no'),  StateFilter(default_state))
async def process_buttons_press(callback: CallbackQuery, state: FSMContext):
    if callback.message.text != 'No':
        await callback.message.answer(text='Продолжайте пользоваться!')
    await callback.answer()

@router.message(StateFilter(FSMFillForm.fill_token))
async def process_token_sent(message: Message, state: FSMContext):
    db.send_vk_token(message.from_user.id, message.text)
    await message.answer("Токен принят", reply_markup=kb.keyboard_main)
    await state.clear()


#Button
@router.message(F.text == "Друзья")
async def friends(message: types.Message):
    await message.answer(
        "Выберете Друга которому хотите написать, для поиска друга отправьте его Имя",
        reply_markup=kb.friends_main)


@router.message(F.text == "Чаты")
async def chat(message: types.Message):
    await message.answer("Выберете чат в который хотите перейти", reply_markup=kb.chat_main)


@router.message(F.text == "Настройки")
async def send_voice_message(message: types.Message):
    pass
