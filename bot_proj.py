import datetime

import telebot
import peewee
from telebot import types
from config import TOKEN_API
from modal import User

bot = telebot.TeleBot(TOKEN_API)
# Comment just for test

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rusbtn = types.KeyboardButton('Русский')
    engbtn = types.KeyboardButton('English')
   # item3 = types.KeyboardButton('Information')
   # item4 = types.KeyboardButton('Other')

    markup.add(rusbtn, engbtn)
    bot.send_message(message.chat.id, ' Welcome to museum`s bot \n Добро пожаловать в бот музея, {0.first_name}! \n Выберите язык \ Select language'.format(message.from_user), reply_markup=markup)
    users_id = [message.chat.id]
    User.create(user_id=message.from_user.id, name=message.from_user.first_name, date=message.date)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Русский':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Работа')
            item2 = types.KeyboardButton('Локация')
            back = types.KeyboardButton('Главное меню')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Русский', reply_markup=markup)
        elif message.text == 'English':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Work')
            item2 = types.KeyboardButton('Location')
            back = types.KeyboardButton('Main menu')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'English', reply_markup=markup)

        # if message.text == 'Русский':
        #     lan = 'Русский'
        # elif message.text == 'English':
        #     lan = 'English'
        #
        #     users_id = [message.chat.id]
        #     User.create(user_id=message.from_user.id, name=message.from_user.first_name)

        elif message.text == 'Work':
            bot.send_message(chat_id=message.chat.id, text='https://victorymuseum.ru/for-visitors/museum-for-china/en/')
            #bot.send_message(message.from_user.id, 'The museum works as follows')
            # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            # item1 = types.KeyboardButton('Information about museum')
            # item2 = types.KeyboardButton('What is up_to in Museum')
            # back = types.KeyboardButton('Go back')
            # markup.add(item1, item2, back)

            #bot.send_message(message.chat.id, 'Work', reply_markup=markup)

        elif message.text == 'Работа':
            bot.send_message(chat_id=message.chat.id, text='https://victorymuseum.ru/for-visitors/museum-for-china/en/')
            #bot.send_message(message.from_user.id, 'Режим работы музея следующий')

            # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            # item1 = types.KeyboardButton('Information about museum')
            # item2 = types.KeyboardButton('What is up_to in Museum')
            # back = types.KeyboardButton('Назад')
            # markup.add(item1, item2, back)
            #bot.send_message(message.chat.id, 'Работа', reply_markup=markup)

        elif message.text == 'Location':
            bot.send_message(message.from_user.id, text='https://victorymuseum.ru/about/contacts/')

        elif message.text == 'Локация':
            bot.send_message(message.from_user.id, text='https://victorymuseum.ru/about/contacts/')

        elif message.text == 'Main menu':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            rusbtn = types.KeyboardButton('Русский')
            engbtn = types.KeyboardButton('English')

            markup.add(rusbtn, engbtn)

            bot.send_message(message.chat.id, 'Main menu', reply_markup=markup)

        elif message.text == 'Главное меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            rusbtn = types.KeyboardButton('Русский')
            engbtn = types.KeyboardButton('English')

            markup.add(rusbtn, engbtn)

            bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)

        if message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Работа')
            item2 = types.KeyboardButton('Локация')
            back = types.KeyboardButton('Главное меню')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)

        elif message.text == 'Go back':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Work')
            item2 = types.KeyboardButton('Location')
            back = types.KeyboardButton('Main menu')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Go back', reply_markup=markup)



        # elif message.text == 'How are you?':
        #     stick = open('C:\Users\User\Desktop\image0132.jpg')
        #     bot.send_photo(message.chat.id, stick)


bot.polling(non_stop=True)

