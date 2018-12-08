ans = []
for something in range(input()):
	n = input()
	l = list(map(int,raw_input().split()))
	min = l[0] + l[1]
	for i in range(n - 1):
		s = l[i] + l[i + 1]
		if s < min:
			min = s
	ans.append(min)
for i in ans:
	print i