# -*- coding: utf-8 -*-
'''
import telebot
import config
bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def default_test(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    url_button = telebot.types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

'''
import config
import telebot
from phrases import *
from menu_function import pizza_call
import markups

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['text'])
def starting_menu(message):
	if message.text == '/start':
		bot.send_message(message.chat.id, start_phrase ,reply_markup = markups.inline_keyboard)
		bot.send_message(message.chat.id, key_board_phrase, reply_markup = markups.keyboard)
	elif message.text == 'Меню':
		bot.send_message(message.chat.id,menu_phrase, reply_markup = markups.menu_kb)
	elif message.text == 'Контакты заведения':
		bot.send_message(message.chat.id, rest_contact)
	else: 
		pass


@bot.callback_query_handler(func=lambda call: True)
def inline_keyboard_query(call):
	if call.message:
		if call.data == 'menu':
			bot.send_message(call.message.chat.id,menu_phrase, reply_markup = markups.menu_kb)
		if call.data == 'rest_contact':
			bot.send_message(call.message.chat.id, rest_contact)
		if call.data == 'pizza':
			pizza_call(call.message.chat.id, bot)
		if call.data == 'meet':
			pass
		if call.data == 'salad':
			pass

if __name__ == '__main__':
     bot.polling(none_stop=True)