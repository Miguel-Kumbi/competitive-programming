from sys import stdin
 
input = stdin.readline
 
n = int(input())
MOD = 1000000007
 
for _ in range(n):
	a, b, c = map(int, input().split())
	bc = pow(b, c, MOD - 1)
	print(pow(a, bc, MOD))
