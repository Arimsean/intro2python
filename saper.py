from random import randint
print "ugadai chislo kotoroe ya zagadayu"
print "vvedi predel chisel"
n = int (raw_input (">"))
x= randint (0,n)
logic = 0
popitka = 1
while (logic != 1):
	
	print "vvedite chislo"
	inp = int (raw_input(">"))
	if x==inp:
		print "ty vuigral", "s" "popitka"
		logic = 1
	else :
		
		print "game over"
		popitka +=1
		print 