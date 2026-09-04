while True:
	B, D = map(int, input().split())

	if not B and not D:
		break

	Bi = list(map(int, input().split()))

	for _ in range(D):
		bd, bc, vd = map(int, input().split())
		Bi[bc - 1] += vd
		Bi[bd - 1] -= vd

	print('S' if all(v >= 0 for v in Bi) else 'N')
