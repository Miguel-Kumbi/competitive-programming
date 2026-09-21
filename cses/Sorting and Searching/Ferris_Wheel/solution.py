import sys

input = sys.stdin.readline

n, x = map(int, input().split())
ni = [int(v) for v in input().split()]
ni.sort()
gondalas = 0
i = 0
j = n - 1
while i <= j:
	if ni[i] + ni[j] <= x:
		i += 1
		j -= 1
	else:
		j -= 1
	gondalas += 1

print(gondalas)
