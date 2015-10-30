s = "Do you speak inglish ?"
d = dict()
for c in s:
	if c not in d:
		d[c] = 1
	else:
		d[c] +=1
print d