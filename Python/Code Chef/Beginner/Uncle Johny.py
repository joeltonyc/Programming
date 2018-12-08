l = []
for something in xrange(input()):
	leng = input()
	a = map(long, raw_input().split())
	k = input()
	ind = a[k - 1]
	a.sort()
	for i in xrange(leng):
		if a[i] == ind:
			pos = i
	l.append(str(pos + 1))
print "\n".join(l)