import sys
 
input = sys.stdin.readline
n = int(input())
for _ in range(n):
	s = input().strip()
	ls = len(s)
	if ls > 10:
		print(f'{s[0]}{ls-2}{s[ls-1]}')
	else:
		print(s)
