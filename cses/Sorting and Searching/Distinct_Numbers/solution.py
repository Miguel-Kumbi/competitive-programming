import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
print(len(set(a)))
