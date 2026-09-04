while True:
	h1, m1, h2, m2 = map(int, input().split())
	if not any(list([h1, m1, h2, m2])):
		break
	begin = (h1 * 60) + m1
	end = (h2 * 60) + m2
	if end <= begin:
		end += 1440
	print(end - begin)
