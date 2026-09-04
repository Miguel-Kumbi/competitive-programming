a, b = map(int, input().split())
ai = [int(v) for v in input().split()]
n = 0
b = ai[b - 1]
for i in ai:
	if i > 0 and i >= b:
		n += 1
print(n)
