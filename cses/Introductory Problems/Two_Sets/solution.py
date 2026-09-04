n = int(input())
sn = ((1 + n) * n) // 2
if sn % 2 != 0:
    print('NO')
else:
    print('YES')
    sn_by_two = sn // 2
    acc = 0
    set1 = list()
    set2 = list()
    for i in range(n, 0, -1):
        if acc + i <= sn_by_two:
                acc += i
                set1.append(i)
        else:
                set2.append(i)
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)
