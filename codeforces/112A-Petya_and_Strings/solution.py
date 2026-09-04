def strcmp(s1, s2) -> int:
	for i, j in zip(s1, s2):
		i = i.lower()
		j = j.lower()
		if i != j:
			break
 
	i = i.lower()
	j = j.lower()
	if ord(j) > ord(i):
		return -1
	elif ord(i) > ord(j):
		return 1
	return 0
 
s1 = input()
s2 = input()
print(strcmp(s1, s2))
