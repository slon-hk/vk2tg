import telebot
from telebot import types
import telebot

from main import hh_ru

bot = telebot.TeleBot('7045965264:AAHjfz-lm4Xr6j1uQh-saK8HYlU_jm59yQk')
specialnost = ""
sity = ""

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton(text="Найти стажировку")
    keyboard.add(button)
    bot.send_message(message.chat.id, "Привет! Нажми кнопку 'Найти стажировку'", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def find_internship(message):
    global specialnost, sity
    if message.text == "Найти стажировку":
        bot.send_message(message.chat.id, "Введите специальность стажировки")
    elif specialnost == "":
        specialnost = message.text
        bot.send_message(message.chat.id, "Введите город стажировки")
    elif sity == "":
        sity = message.text
        staz = hh_ru(specialnost, 1)
        keyboard = types.InlineKeyboardMarkup()
        url_button_0 = types.InlineKeyboardButton(text=str(staz[0][1]+", "+str(staz[0][0])+", "+str(staz[0][2])+"₽"), url=str(staz[0][4]))
        url_button_1 = types.InlineKeyboardButton(text=str(staz[1][1]+", "+str(staz[1][0])+", "+str(staz[1][2])+"₽"), url=str(staz[1][4]))
        url_button_2 = types.InlineKeyboardButton(text=str(staz[1][1]+", "+str(staz[2][0])+", "+str(staz[2][2])+"₽"), url=str(staz[2][4]))
        url_button_3 = types.InlineKeyboardButton(text=str(staz[2][1]+", "+str(staz[3][0])+", "+str(staz[3][2])+"₽"), url=str(staz[3][4]))
        url_button_4 = types.InlineKeyboardButton(text=str(staz[4][1]+", "+str(staz[4][0])+", "+str(staz[4][2])+"₽"), url=str(staz[4][4]))
        url_button_5 = types.InlineKeyboardButton(text=str(staz[5][1]+", "+str(staz[5][0])+", "+str(staz[5][2])+"₽"), url=str(staz[5][4]))
        url_button_6 = types.InlineKeyboardButton(text=str(staz[6][1]+", "+str(staz[6][0])+", "+str(staz[6][2])+"₽"), url=str(staz[6][4]))
        url_button_7 = types.InlineKeyboardButton(text=str(staz[7][1]+", "+str(staz[7][0])+", "+str(staz[7][2])+"₽"), url=str(staz[7][4]))
        url_button_8 = types.InlineKeyboardButton(text=str(staz[8][1]+", "+str(staz[8][0])+", "+str(staz[8][2])+"₽"), url=str(staz[8][4]))
        url_button_9 = types.InlineKeyboardButton(text=str(staz[9][1]+", "+str(staz[9][0])+", "+str(staz[9][2])+"₽"), url=str(staz[9][4]))
        keyboard.add(url_button_0)
        keyboard.add(url_button_1)
        keyboard.add(url_button_2)
        keyboard.add(url_button_3)
        keyboard.add(url_button_4)
        keyboard.add(url_button_5)
        keyboard.add(url_button_6)
        keyboard.add(url_button_7)
        keyboard.add(url_button_8)
        keyboard.add(url_button_9)
        bot.send_message(message.chat.id, "Выберее стажировку", reply_markup=keyboard)

while 1:
    try:
        bot.polling()
    except:
        bot.send_message(message.chat.id, "Ошибочка")
        bot.polling()