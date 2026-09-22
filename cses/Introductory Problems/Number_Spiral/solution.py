import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
	x, y = map(int, input().split())
	n = max(x, y)
	if n % 2 == 0:
		if x == n:
			pos_xy = n*n - y + 1
		else:
			pos_xy = (n-1)*(n-1) + x
	else:
		if y == n:
			pos_xy = n*n - x + 1
		else:
			pos_xy = (n-1)*(n-1) + y
	print(pos_xy)
