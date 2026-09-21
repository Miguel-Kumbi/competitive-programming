import sys

input = sys.stdin.readline

def two_pointer(array: list, n: int, at) -> str:
	l = 0
	r = n - 1
	
	while l < r:
		_sum = array[l][0] + array[r][0]
		if _sum == target:
			return f'{array[l][1] + 1} {array[r][1] + 1}'
		elif _sum < target:
			l += 1
		else:
			r -= 1
	return 'IMPOSSIBLE'

n, target = map(int, input().split())
ni = [int(v) for v in input().split()]
ni = [[ni[i], i] for i in range(n)]
ni.sort()
print(two_pointer(ni, n, target))
