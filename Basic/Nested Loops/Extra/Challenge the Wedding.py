men = int(input())
women = int(input())
tables = int(input())


for i in range(1, men +1):
    for j in range(1, women +1):
        if tables == 0:
            break
        else:
            print(f'({i} <-> {j})', end = ' ')
            tables -= 1