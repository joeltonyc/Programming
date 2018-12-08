a, b = map(int, raw_input().split())
d = str(a - b)
c = 0
s = d[0]
if s != "5":
	s = "5"
else:
	s = "4"
d = s + d[1:len(d)]
print d