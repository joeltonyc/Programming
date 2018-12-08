n = int(input())
l = []
d = []
while n>1:
	for x in range(2, n+1):
		if n%x==0:
			l.append(x)
			print x
			n/=x
			break
b = 2
count = 0
for x in l:
	a = x
	if a==b:
		d.append(a)
		b += 1
		count += 1