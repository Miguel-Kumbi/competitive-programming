import math
import itertools
 
s = input()
unicas = sorted(set(itertools.permutations(s)))
print(len(unicas))
for p in unicas:
    print(''.join(p))
