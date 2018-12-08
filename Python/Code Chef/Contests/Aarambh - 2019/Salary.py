#https://www.codechef.com/AARA2018/problems/ARMBH1
ans = []
for i in xrange(long(raw_input())):
	x, n = map(long, raw_input().split())
	l = []
	for i in range(x, (n + 1)):
		if i % x == 0:
			l.append(i)
	ans.append(str(sum(l)))
print '\n'.join(ans)