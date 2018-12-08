for x in range(input()):
	n = input()
	c = 0
	while n > 0:

		if n >= 100:
			c += 1
			n -= 100
			continue

		elif n >= 50:
			c += 1
			n -= 50
			continue

		elif n >= 10:
			c += 1
			n -= 10
			continue

		elif n >= 5:
			c += 1
			n -= 5
			continue

		elif n >= 2:
			c += 1
			n -= 2
			continue

		elif n >= 1:
			c += 1
			n -= 1
			continue

	print c