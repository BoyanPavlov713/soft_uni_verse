number = int(input())
password = 0
code = ''

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a < b and d < c) and (a * b + c * d == number):
                    password += 1
                    print(f'{a}{b}{c}{d}', end=' ')
                    if password == 4:
                        code = f'{a}{b}{c}{d}'
if password >= 4:
    print()
    print(f'Password: {code}')
if password < 4:
    print()
    print('No!')
