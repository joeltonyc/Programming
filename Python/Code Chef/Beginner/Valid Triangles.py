for x in range(input()):
	a, b, c = map(int, raw_input().split())
	if a == 0 or b == 0 or c == 0:
		print "NO"
	else:
		if (a + b + c) == 180:
			print "YES"
		else:
			print "NO"