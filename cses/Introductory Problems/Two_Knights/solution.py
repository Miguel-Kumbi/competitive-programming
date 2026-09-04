n = int(input())
 
for k in range(1, n + 1):
    all_form = (((k ** 2) - 1) * (k ** 2)) / 2
    all_atacks = 4 * (k - 1) * (k - 2)
    result = int(all_form - all_atacks)
    print(result)
