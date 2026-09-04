n = int(input())
for _ in range(n):
	a = int(input())
	ai = [int(v) for v in input().split()]
	s_ai = sum(ai)
	if a % 2 == 0 and s_ai % 4 == 0:
		print('YES')
	else:
		print('NO')
