n = int(input())
a = 0
b = 1
for x in range(n):
	print a+b
	if a<b:
		a = a+b
	else:
		b = a+b