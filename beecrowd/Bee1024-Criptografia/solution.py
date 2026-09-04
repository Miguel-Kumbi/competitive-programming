def first_pass(s):
	for i in range(0, len(s)):
		if (s[i].isalpha()):
			s[i] = chr(ord(s[i]) + 3)
def second_pass(s):
	s.reverse()

def third_pass(s):
	half = int((len(s)) / 2)
	i = half
	for i in range(half, len(s)):
		s[i] = chr(ord(s[i]) - 1)

N = int(input())

for c in range(0, N):
	M = list(input())
	first_pass(M)
	second_pass(M)
	third_pass(M)
	print(''.join(M))
