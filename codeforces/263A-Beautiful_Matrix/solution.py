matrix = list()
for _ in range(5):
	matrix.append(input().split())
 
for l in range(5):
	try:
		c = matrix[l].index('1')
	except ValueError:
		c =  -1
	if c >= 0:
		break
 
if c != -1:
	moves = abs(l - 2) + abs(c - 2)
	print(moves)
