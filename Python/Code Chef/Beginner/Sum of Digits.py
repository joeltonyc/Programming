def Sum_Of_Digits(Number):
    Sum = 0
    while(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        Number = Number //10
    return Sum

l = []
n = int(input())
for i in range(n):
	num = int(input())
	l.append(Sum_Of_Digits(num))
for i in range(len(l)):
	print l[i]