for x in range(input()):
	n = raw_input()
	l = []
	for a in n:
		l.append(a)
	l = map(int, l)
	c = 0
	for i in l:
		if i == 4:
			c += 1
	print c