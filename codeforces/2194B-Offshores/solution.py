N = int(input())
for _ in range(0, N):
	n, x, y = map(int, input().split())
	ni = list(map(int, input().split()))
	total = sum(i // x for i in ni)
	acc = 0
	for i in ni:
		contrib = total - (i // x)
		if (i + contrib * y) > acc:
			acc = i + contrib * y
	print(acc)
