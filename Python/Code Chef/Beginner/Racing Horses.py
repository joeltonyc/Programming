l = []
for something in xrange(input()):
	n = input()
	a = list(map(long, raw_input().split()))
	a.sort()
	m = a[1] - a[0]
	for i in xrange(n - 1):
		d = a[i + 1] - a[i]
		if d < m:
			m = d
	l.append(str(m))
print "\n".join(l)