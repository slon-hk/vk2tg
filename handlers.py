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
    fill_token = State()
    fill_msg = State()
    await_comm = State()
    yes_no = State()

@router.message(CommandStart(), StateFilter(default_state))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Привет Это бот Vk2Tg, он позволяет тебе общаться с твоими друзьями в Вк не уходя из телеграмма")
    db.db_start()
    if db.filtr_db(message.from_user.id) == False:
        await message.answer(text='Введите токен')
        await state.set_state(FSMFillForm.fill_token)
    else:
        await message.answer(text='Вы уже зарегестрированны.\nХотите изменить токен?', reply_markup=kb.yes_main)

@router.message(StateFilter(FSMFillForm.fill_token))
async def process_token_sent(message: Message, state: FSMContext):
    db.send_vk_token(message.from_user.id, message.text)
    await message.answer("Токен принят", reply_markup=kb.keyboard_main)
    await message.answer(text=db.return_db())
    await state.clear()

@router.message(F.text == "yes")
async def friends(message: types.Message):
    await message.answer(
        "Выберете Друга которому хотите написать, для поиска друга отправьте его Имя",
        reply_markup=kb.friends_main)

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
