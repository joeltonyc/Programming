for x in range(input()):
	a, b = map(int, raw_input().split())
	if a == b:
		print '='
	elif a > b:
		print '>'
	elif a < b:
		print '<'