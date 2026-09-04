from collections import Counter
 
def is_anagram(s, t):
	return Counter(s) == Counter(t)
	
n = int(input())
 
for _ in range(n):
	n_chars = int(input())
	_str, name = map(str, input().split())
	
	print('YES' if is_anagram(_str, name) else 'NO')
