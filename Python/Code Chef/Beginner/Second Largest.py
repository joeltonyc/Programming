for i in range(input()):
	l = []
	a, b, c = raw_input().split()
	l.append(int(a))
	l.append(int(b))
	l.append(int(c))
	l.remove(min(l))
	l.remove(max(l))
	l = map(str, l)
	print ''.join(l)