# -*- coding: utf-8 -*-
print u"привет vyberi 1# or 2#"
door = raw_input (">>>")

if door == "1":
	print u"ЗАЧЕМ ТУТ?"
	print u"1.ТЫ ТРУП."
	print u"2.ТЫ ОВОЩЬ."
	
	g==raw_input("> ")

	if g == "1":
		print u"НАЧНЕМ С НОГИ"
	elif g == "2":
		print u"НАЧНЕМ С РУКИ"
	else:
		print u"ХОТЕЛ СБЕЖАТЬ?" % g

elif door == "2":
	print u"ЗРЯ ТЫ СЮДА ПОПАЛ"
	print u"ВЫБИРАЙ УБЬЕШЬ ИЛИ УМРЕШЬ?"
	print u"1.УБЬЮ!"
	print u"2.УМРУ!"
	print u"3.НЕ ХОЧУ УМИРАТЬ И УБИВАТЬ!"

	inst = raw_input("> ")

