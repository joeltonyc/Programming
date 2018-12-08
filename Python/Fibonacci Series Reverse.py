l = []
n = int(input())
a = 0
b = 1
for x in range(n):
	if a<b:
		a = a+b
		l.append(str(a))
	else:
		b = a+b
		l.append(str(b))
l = l[::-1]
print ' '.join(l)