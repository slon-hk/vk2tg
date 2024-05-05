from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from main import friends

keyboard_button = [
    [KeyboardButton(text="Друзья"), KeyboardButton(text="Чаты")],
    [KeyboardButton(text="Найстройки"), KeyboardButton(text="Профиль")],
]
main = ReplyKeyboardMarkup(
    keyboard=keyboard_button,
    resize_keyboard=True,
    input_field_placeholder="Выберете пункт меню!",
)

page_count = 0
friends = friends(1)
friends_button = [
    [
        InlineKeyboardButton(
            text=f"{friends[page_count][0]} {friends[page_count][1]}",
            callback_data=f"{friends[page_count][2]}",
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{friends[page_count][0]} {friends[page_count][1]}",
            callback_data=f"{friends[page_count][2]}",
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{friends[page_count][0]} {friends[page_count][1]}",
            callback_data=f"{friends[page_count][2]}",
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{friends[page_count][0]} {friends[page_count][1]}",
            callback_data=f"{friends[page_count][2]}",
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{friends[page_count][0]} {friends[page_count][1]}",
            callback_data=f"{friends[page_count][2]}",
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{friends[page_count][0]} {friends[page_count][1]}",
            callback_data=f"{friends[page_count][2]}",
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{friends[page_count][0]} {friends[page_count][1]}",
            callback_data=f"{friends[page_count][2]}",
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{friends[page_count][0]} {friends[page_count][1]}",
            callback_data=f"{friends[page_count][2]}",
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{friends[page_count][0]} {friends[page_count][1]}",
            callback_data=f"{friends[page_count][2]}",
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{friends[page_count][0]} {friends[page_count][1]}",
            callback_data=f"{friends[page_count][2]}",
        )
    ],
    [
        InlineKeyboardButton(text="<=", callback_data="<="),
        InlineKeyboardButton(text="=>", callback_data="=>"),
    ],
]
friends = InlineKeyboardMarkup(inline_keyboard=friends_button, resize_keyboard=True)

chat = friends(1)
chat_button = [
    [
        InlineKeyboardButton(
            text=f"{friends[page_count][0]} {friends[page_count][1]}",
            callback_data=f"{friends[page_count][2]}",
        )
    ]]
chat = InlineKeyboardMarkup(inline_keyboard=chat_button, resize_keyboard=True)
