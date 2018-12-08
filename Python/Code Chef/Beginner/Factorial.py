a = []
def Z(n):
	c = 0
	i = 5
	div = n / i
	while div >= 1:
		div = n / i
		c += long(div)
		i *= 5
	return long(c)
for x in xrange(long(raw_input())):
	a.append(str(Z(long(raw_input()))))
print "\n".join(a)