for x in range(input()):

	amt = input()

	c = 0

	while amt > 0:

		if amt >= 2048:
			c += 1
			amt -= 2048
			continue

		elif amt >= 1024:
			c += 1
			amt -= 1024
			continue

		elif amt >= 512:
			c += 1
			amt -= 512
			continue

		elif amt >= 256:
			c += 1
			amt -= 256
			continue

		elif amt >= 128:
			c += 1
			amt -= 128
			continue

		elif amt >= 64:
			c += 1
			amt -= 64
			continue

		elif amt >= 32:
			c += 1
			amt -= 32
			continue

		elif amt >= 16:
			c += 1
			amt -= 16
			continue

		elif amt >= 8:
			c += 1
			amt -= 8
			continue

		elif amt >= 4:
			c += 1
			amt -= 4
			continue

		elif amt >= 2:
			c += 1
			amt -= 2
			continue

		elif amt >= 1:
			c += 1
			amt -= 1
			continue

	print c