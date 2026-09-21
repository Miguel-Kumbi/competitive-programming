import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
desejados = [int(v) for v in input().split()]
disponiveis = [int(v) for v in input().split()]
desejados.sort()
disponiveis.sort()
i = 0
j = 0
rented = 0
while i < n and j < m:
	if disponiveis[j] >= (desejados[i] - k) and disponiveis[j] <= (desejados[i] + k):
		rented += 1
		i += 1
		j += 1
	elif disponiveis[j] < desejados[i] - k:
		j += 1
	else:
		i += 1
print(rented)

