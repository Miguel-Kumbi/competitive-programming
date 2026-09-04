
a = input()
b = input()
 
for c in range(0, len(a)):
    print('0' if a[c] == b[c] else '1', end = '')
