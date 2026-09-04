n = int(input())
passes = 0
while n > 0:
	if n >= 5:
		n -= 5
		passes += 1
	elif n >= 4:
		n -= 4
		passes += 1
	elif n >= 3:
		n -= 3
		passes += 1
	elif n >= 2:
		n -= 2
		passes += 1
	else:
		n -= 1
		passes += 1
print(passes)
