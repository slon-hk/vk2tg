from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram import F, Router
import asyncio

import keyboard as kb

bot = Bot(token="7120855483:AAHwJejnkJ-beolR8mfWBI4sydyL0YZDWuc")
router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет Это бот Vk2Tg, он позволяет тебе общаться с твоими друзьями в Вк не уходя из телеграмма",
        reply_markup=kb.main,
    )


@router.message(F.text == "Друзья")
async def friends(message: types.Message):
    await message.answer(
        "Выберете Друга которому хотите написать, для поиска друга отправьте его Имя",
        reply_markup=kb.friends,
    )
