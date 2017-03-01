# -*- coding: utf-8 -*-
# реализация функционала кнопки 'Меню'

import telebot
from phrases import peperoni_ph, gavai_ph, halapenu_ph
from file_id import peperoni, gavai, halapenu
import markups


def pizza_call(chat,tel):
	pizza = {peperoni: peperoni_ph,
			 gavai: gavai_ph,
			 halapenu: halapenu_ph}
	for key in pizza.keys():
		tel.send_photo(chat,key)
		tel.send_message(chat,text = pizza.get(key), reply_markup = markups.basket)














