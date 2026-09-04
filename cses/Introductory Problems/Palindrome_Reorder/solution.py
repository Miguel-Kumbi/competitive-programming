from collections import Counter
import sys
 
input = sys.stdin.readline
 
s = input().strip()
begin = ''
end = ''
n_impar = 0
char_impar = ''
q_char_impar = 0
 
for v, t in Counter(s).items():
	if t % 2 != 0:
		n_impar += 1
		char_impar = v
		q_char_impar = t
	else:
		begin += v * (t // 2)
		end = v * (t // 2) + end
if n_impar > 1:
	print('NO SOLUTION')
else:
	begin += char_impar * q_char_impar
	print(begin+end)
