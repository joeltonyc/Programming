n, k = raw_input().split(" ")
n = int(n)
k = int(k)
c = 0
for i in range(n):
	x = int(input())
	if x%k==0:
		c+=1
print c