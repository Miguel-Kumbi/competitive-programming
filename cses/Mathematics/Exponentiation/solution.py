from sys import stdin
 
input = stdin.readline
 
n = int(input())
MOD = 1000000007
 
for _ in range(n):
	a, b = map(int, input().split())
	print(pow(a, b, MOD))
