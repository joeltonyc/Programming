n = int(input())
l = list(str(n).split())
s = 0
if len(str(n)) != 3:
	print False
else:
	for int(i) in l:
		iPow = i**3
		s += iPow
	if s == n:
		print True
	else:
		print False
