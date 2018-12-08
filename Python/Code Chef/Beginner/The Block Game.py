for x in range(input()):
	l = list(raw_input())
	lR = l[::-1]
	lS = map(int, ''.join(l))
	lRS = map(int, ''.join(lR))
	if lS == lRS:
		print "wins"
	else:
		print "losses"