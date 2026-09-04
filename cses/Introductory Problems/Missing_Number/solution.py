import sys
 
input = sys.stdin.readline
n = int(input())
ni = [int(i) for i in input().split()]
all_n = [int(i) for i in range(1, n + 1)]
 
print(sum(all_n) - sum(ni))
