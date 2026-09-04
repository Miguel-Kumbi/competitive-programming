import sys
 
input = sys.stdin.readline
s = input()
ant = s[0]
rep = 0
_max = 0
 
for c in s:
	if c == ant:
		rep += 1
		if rep > _max: _max = rep
	else:
		rep = 1
	ant = c
print(_max)
