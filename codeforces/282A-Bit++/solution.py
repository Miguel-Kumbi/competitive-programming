N = int(input())
num = 0
 
for _ in range(N):
	exp = input()
	if exp == '++X' or exp == 'X++':
		num += 1
	else:
		num -= 1
print(num)
