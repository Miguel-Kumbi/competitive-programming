import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
	a, b = map(int, input().split())
	print('YES' if (a + b) % 3 == 0 and a <= 2 * b and b <= 2 * a else 'NO')
