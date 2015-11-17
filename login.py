import datetime
import sys
import os


print "vvedite login",
login = raw_input(":")
print "vvedite parol",
parol = raw_input(":")
if login == "admin" and parol == "12345":
	now_date = datetime.date.today()
	print now_date 
	year = now_date.year
	print os.name
else:
	print "nevernyi login ili parol"