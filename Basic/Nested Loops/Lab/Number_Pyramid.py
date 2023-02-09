n = int(input())
current = 1
current_bigger_n = False

for r in range(1, n +1):
    for c in range(1, r +1):
        if current > n:
            current_bigger_n = True
            break
        print(str(current) + ' ', end='')
        current += 1
    if current_bigger_n:
        break
    print()



