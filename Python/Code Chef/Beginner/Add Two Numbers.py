l = []
n = int(input())
for i in range(n):
	n1, n2 = raw_input().split()
	l.append(str(int(n1)+int(n2)))
for i in range(len(l)):
	print l[i]