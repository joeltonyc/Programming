l = []
n = input()

for i in range(n):
    l.append(float(input()))

ans = sorted(l)
print ans[::-1]
