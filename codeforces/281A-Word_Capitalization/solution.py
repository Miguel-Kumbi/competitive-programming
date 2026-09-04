
import sys
 
input = sys.stdin.readline
s = list(input().strip())
if s[0].islower():
	s[0] = s[0].upper()
	print(''.join(s))
else:
	print(''.join(s))
