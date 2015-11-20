# -*- coding: utf-8 -*-
import datetime
import sys
import os
import time
from random import randint 

popytka = 0

cit1 = u"Счастье — это когда родные и очень близкие тебе люди здоровы ! Остальное отремонтируем, выбросим, купим, забудем…"

cit2 = u"Бросая бумеранг поступков, заранее думай, как будешь ловить бумеранг последствий."

cit3 = u"Кто не стучится - тому не открывают. Кто не пробует - у того не получается."

while popytka <= 3:

	print "vvedite login",
	login = raw_input(":")
	print "vvedite parol",
	parol = raw_input(":")


	if login == "admin" and parol == "12345":
		now_date = datetime.date.today()
		print now_date 
		year = now_date.year
		print os.name
		break
	else:
		print "nevernyi login ili parol"
	popytka += 1
	time.sleep(3)

	citata = randint(1,3)
	if citata == 1:
		print cit1
	elif citata == 2:
		print cit2
	else:
		print cit3
	print "net tak net"