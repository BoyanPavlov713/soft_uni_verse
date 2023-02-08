def fac_func(a, b):
    first_factorial = 1
    second_factorial = 1

    for i in range(1, int1 + 1):
        first_factorial *= i
    for j in range(1, int2 + 1):
        second_factorial *= j
    print(f'{first_factorial / second_factorial: .02f}')


int1 = int(input())
int2 = int(input())
fac_func(5, 2)

