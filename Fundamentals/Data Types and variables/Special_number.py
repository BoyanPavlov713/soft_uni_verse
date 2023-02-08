number = int(input())

for i in range(1, number + 1):
    flag = False
    num_as_string = str(i)
    total = 0
    for ch in num_as_string:
        total += int(ch)
    if total == 5 or total == 7 or total == 11:
        flag = True
    print(f'{i} -> {flag}')

