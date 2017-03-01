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
