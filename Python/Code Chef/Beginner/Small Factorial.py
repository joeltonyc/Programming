def fact(n):
	fact = 1
	for i in range(1, (n + 1)):
		fact *= i
	return fact

for x in range(input()):
	print fact(input())