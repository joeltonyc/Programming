 l = []
for something in range(input()):
	input()
	f = ind = False
	s = raw_input()
	for i in s:
		if i == 'Y':
			f = True
			break
		elif i == 'I':
			ind = True
			break
	if f:
		l.append("NOT INDIAN")
	elif ind:
		l.append("INDIAN")
	else:
		l.append("NOT SURE")
for i in l:
	print i