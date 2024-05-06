from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from main import friends

keyboard_button = [
    [KeyboardButton(text="Друзья"), KeyboardButton(text="Чаты")],
    [KeyboardButton(text="Настройки"), KeyboardButton(text="Профиль")],
]
main = ReplyKeyboardMarkup(
    keyboard=keyboard_button,
    resize_keyboard=True,
    input_field_placeholder="Выберете пункт меню!",
)

friends_list = friends(1)
friend = [
    [InlineKeyboardButton(text=friends_list[0], callback_data=friends_list[1])],
    [InlineKeyboardButton(text=friends_list[0], callback_data=friends_list[1])],
    [InlineKeyboardButton(text=friends_list[0], callback_data=friends_list[1])],
    [InlineKeyboardButton(text=friends_list[0], callback_data=friends_list[1])],
    [InlineKeyboardButton(text=friends_list[0], callback_data=friends_list[1])],
    [InlineKeyboardButton(text=friends_list[0], callback_data=friends_list[1])],
    [InlineKeyboardButton(text=friends_list[0], callback_data=friends_list[1])],
    [InlineKeyboardButton(text=friends_list[0], callback_data=friends_list[1])],
    [InlineKeyboardButton(text=friends_list[0], callback_data=friends_list[1])],
    [InlineKeyboardButton(text=friends_list[0], callback_data=friends_list[1])],
    [
        InlineKeyboardButton(text="<-", callback_data="behind"),
        InlineKeyboardButton(text="->", callback_data="next"),
    ],
]

friends_main = InlineKeyboardMarkup(
    keyboard=friend,
    resize_keyboard=True,
    input_field_placeholder="Найдите своих друзей",
)
