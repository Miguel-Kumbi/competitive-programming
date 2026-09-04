N = int(input())
num = 0
 
for _ in range(N):
	exp = input()
	if exp in ['1 1 1', '0 1 1', '1 0 1', '1 1 0']:
		num += 1
print(num)
