from math import sqrt
import sys
 
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
 
def has_three_divisor(v):
    if v == 1:
        return False
    r = int(sqrt(v))
    return r * r == v and is_prime(r)
 
input = sys.stdin.readline
 
n = int(input())
values = [int(v) for v in input().split()]
for v in values:
	if has_three_divisor(v):
		print('YES')
	else:
		print('NO')
