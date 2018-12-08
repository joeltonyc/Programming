withHoles = ['Q', 'R', 'O', 'P', 'A', 'D', 'B']
for z in range(input()):
	s = raw_input()
	c = 0
	for i in s:
		if i in withHoles:
			c += 1
	print c