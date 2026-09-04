s = sorted(input())
ls = len(s)
for i in range(ls):
	if i == ls - 1:
		print(s[i])
	elif s[i] != '+':
		print(s[i], end='+')
