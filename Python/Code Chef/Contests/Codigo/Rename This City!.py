#https://www.codechef.com/COG2018/problems/COG1803
ans = []
for i in xrange(long(raw_input())):
	raw_input()
	l = raw_input().split()
	if l.count('1') >= l.count('-1'):
		ans.append("YES")
	else:
		ans.append("NO")
print "\n".join(ans)