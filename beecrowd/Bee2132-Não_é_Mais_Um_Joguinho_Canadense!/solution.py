words = 1

while True:
	try:
		acc = 1
		q = False
		first = True
		total = 0
		s = list(input())
		for _ in range(s.count('b')):
			for c in s:
				if c == 'b':
					q = True
				if q == True:
					if first == True:
						first = False
					else:
						acc *= 2
			if q == False:
				acc = 0
			total += acc
			q = False
			first = True
			acc = 1
			s.remove('b')
		
		print(f'Palavra {words}\n{total}\n')
		words += 1
	except EOFError:
		exit(0)
