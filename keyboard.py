from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from main import friends, chat_list

# UNDER BUTTON
keyboard_button = [
    [KeyboardButton(text="Друзья"), KeyboardButton(text="Чаты")],
    [KeyboardButton(text="Настройки"), KeyboardButton(text="Профиль")]]

keyboard_main = ReplyKeyboardMarkup(keyboard=keyboard_button, resize_keyboard=True, input_field_placeholder="Выберете пункт меню!")

# FRIENDS LIST
friends_list = friends(1)
friend_button = []

for i in range(len(friends_list)):
    friend_button.append([InlineKeyboardButton(text=friends_list[i][0], callback_data=str(friends_list[i][1]))])

friend_button.append([InlineKeyboardButton(text="<-", callback_data="behind"),InlineKeyboardButton(text="->", callback_data="next"),])
friends_main = InlineKeyboardMarkup(inline_keyboard=friend_button, resize_keyboard=True)

# CHAT LIST
chat_list = chat_list()
chat_button = []

for i in range(len(chat_list)):
    chat_button.append(
        [InlineKeyboardButton(text=f"{chat_list[i][0]}: {chat_list[i][2]}", callback_data=str(chat_list[i][1]))])

chat_button.append(
    [InlineKeyboardButton(text="<-", callback_data="behind"), InlineKeyboardButton(text="->", callback_data="next")])

chat_main = InlineKeyboardMarkup(inline_keyboard=chat_button, resize_keyboard=True)

#YES OR NO
yes_button = [[InlineKeyboardButton(text="Да", callback_data="yes"),InlineKeyboardButton(text="Нет", callback_data="no"),]]
yes_main = InlineKeyboardMarkup(inline_keyboard=yes_button, resize_keyboard=True)