d = []
l = list(raw_input())
if l[0]=='0':
  print False
  exit()
for i in l:
	if i in d:
		print False
		exit()
	else:
		d.append(i)
print True