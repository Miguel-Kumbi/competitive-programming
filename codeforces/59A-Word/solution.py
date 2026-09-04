word = input()
uppers = 0
lowers = 0
 
for l in word:
	if l.isupper():
		uppers += 1
	elif l.islower():
		lowers += 1
 
if uppers > lowers:
	print(word.upper())
else:
	print(word.lower())
