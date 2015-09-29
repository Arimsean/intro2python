print "vvedite tekushii god",
cyear = raw_input (">")
print "vvedite god rojdenia"
byear = raw_input (">")
age = int (cyear) - int (byear)
print "vash vozrast",age
if age > 0 and age <=6:
	print "idi v det sad"
if age > 7 and age <=17:
	print "uchis v shkole horosho"
if age > 18 and age <=19:
	print "podumai postupit ili rabotat"
if age > 20 and age <=24:
	print "ty student ili ty rabotaesh"
if age > 25 and age <=35:
	print "ty jenilsya i rabotaew"
if age > 36 and age <=45:
	print "u tebya est deti"
if age > 46 and age <=70:
	print "ty hochew spokoino do zhit do 100"
if age > 70 and age <=90:
	print "ty pencioner"
