input()
l = list(map(int, raw_input().split()))
ce = co = 0
for i in l:
	if i % 2 == 0:
		ce += 1
	else:
		co += 1
if ce > co:
	print "READY FOR BATTLE"
else:
	print "NOT READY"