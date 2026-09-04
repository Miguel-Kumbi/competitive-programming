def	ft_total(digit):
	if int(digit) == 0:
		return digit + 6
	elif int(digit) == 1:
		return 2
	elif int(digit) == 2:
		return 5
	elif int(digit) == 3:
		return 5
	elif int(digit) == 4:
		return 4
	elif int(digit) == 5:
		return 5
	elif int(digit) == 6:
		return 6
	elif int(digit) == 7:
		return 3
	elif int(digit) == 8:
		return 7
	elif int(digit) == 9:
		return 6


n = int(input())
for _ in range(0, n):
	num = input()
	total_leds = 0
	for digit in num:
		total_leds = total_leds + ft_total(int(digit))
	print(f'{total_leds} leds')
