# -*- coding: utf-8 -*-
# клавиатуры бота

import telebot

# клавиатура для меню
menu_kb = telebot.types.InlineKeyboardMarkup()
menu_kb.add(telebot.types.InlineKeyboardButton(text='пицца', callback_data='pizza'))
menu_kb.add(telebot.types.InlineKeyboardButton(text='стейки', callback_data='meet'))
menu_kb.add(telebot.types.InlineKeyboardButton(text='салаты', callback_data='salad'))

# добавить в карзину, убрать из карзины, кол-во в карзине
basket = telebot.types.InlineKeyboardMarkup()
remove = telebot.types.InlineKeyboardButton(text = '-', callback_data = 'remove')
amount = telebot.types.InlineKeyboardButton(text = '()', callback_data = 'amount')
add = telebot.types.InlineKeyboardButton(text = '+', callback_data = 'add')
basket.row(remove, amount, add)
basket.add(telebot.types.InlineKeyboardButton(text = 'Моя корзина', callback_data= 'basket'))
basket.add(telebot.types.InlineKeyboardButton(text='Меню', callback_data='menu'))


# Стартовая клавиатуры

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) # обычная клавиатура
keyboard.row('Меню')
keyboard.row('Моя корзина')
keyboard.row('Контакты заведения')

inline_keyboard = telebot.types.InlineKeyboardMarkup() # кнопки чата
inl_button1 = telebot.types.InlineKeyboardButton(text = 'Меню', callback_data='menu')
inline_keyboard.add(inl_button1)
inl_button2 = telebot.types.InlineKeyboardButton(text = 'Моя корзина',callback_data='order')
inline_keyboard.add(inl_button2)
inl_button3 = telebot.types.InlineKeyboardButton(text = 'Контакты заведения',callback_data='rest_contact')
inline_keyboard.add(inl_button3)