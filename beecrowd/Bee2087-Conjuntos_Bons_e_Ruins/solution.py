while True:
	n = int(input())
	if n == 0: break
	msg = True
	strs = [input() for _ in range(n)]
	strs.sort()
	for i in range(n - 1):
		if strs[i + 1].startswith(strs[i]):
			msg = False
			break
	print('Conjunto Bom' if msg else 'Conjunto Ruim')
