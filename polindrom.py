print "vedi slovo"
l = list (raw_input ("->"))
M = l[:]
N = []
for x in reversed(M):
	N.append(x)
if l == N:
	print "polindrom"
else:
	print "ne polindrom"