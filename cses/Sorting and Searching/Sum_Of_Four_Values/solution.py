import sys

def two_pointer(arr: list, n: int, target: int) -> str:
	for i in range(n-3):
		for j in range(i+1, n-2):
			l = j + 1
			r = n - 1
			while l < r:
				_sum = arr[i][0] + arr[j][0] + arr[l][0] + arr[r][0]
				if _sum == target:
					return f'{arr[i][1] + 1} {arr[j][1] + 1} {arr[l][1] + 1} {arr[r][1] + 1}'
				elif _sum < target:
					l += 1
				else:
					r -= 1
	return 'IMPOSSIBLE'

input = sys.stdin.readline

n, target = map(int, input().split())
ni = [int(v) for v in input().split()]
ni = [[ni[i], i] for i in range(n)]
ni.sort()
print(two_pointer(ni, n, target))
