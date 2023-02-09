def fac_func(a, b):
    first_factorial = 1
    second_factorial = 1

    for i in range(1, int1 + 1):
        first_factorial *= i
    for j in range(1, int2 + 1):
        second_factorial *= j
    result = first_factorial / second_factorial
    return result


def write_fuc (number):
     print(f'{number: .02f}')


int1 = int(input())
int2 = int(input())
num = fac_func(a = int1 , b = int2)
write_fuc(num)

