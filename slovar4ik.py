def s():
	print "dlya prosmotra slovarya najmi 1"
	print "dlya dobavlenia slova v slovar najmi 2"


def f():
	choise = raw_input(">>>>")
	if choise == "1":
			for key in d:
				print key, " - ", d[key]
	elif choise =="2":
		while add == "1":
			print "vvedite slovo na english"
			dkey = raw_input (">>>")
			if dkey not in d:
				print "vvedite perevod"
			else:
				print "vvedite drugoe slovo. %s uje v slovare est" % dkey
				dval = raw_input (">>>")
				d[dkey] = dval
				for key in d:
					print key, " - ", d[key]



d = {'cat':'kowka','dog':'sobaka','snake':'zmeya'}
print d
s()
add = "1"
f()
print d
		else:
		s()
choise = raw_input(">>>>")
	