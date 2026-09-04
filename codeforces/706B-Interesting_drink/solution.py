from bisect import bisect_right
 
n = int(input())
ni = list(map(int, input().split()))
ni.sort()
q = int(input())
 
for _ in range(q):
	mi = int(input())
	print(bisect_right(ni, mi))
