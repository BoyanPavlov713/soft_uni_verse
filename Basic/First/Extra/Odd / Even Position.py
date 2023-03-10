import sys

n = int(input())
odd_sum = 0
odd_min = 10000000000
odd_max = -10000000000
even_sum = 0
even_min = 1000000000
even_max = -1000000000


for i in range(1, n+1):
    number = float(input())
    if i % 2 != 0:
        odd_sum += number
        if number < odd_min:
            odd_min = number
        if number > odd_max:
            odd_max = number

    elif i % 2 == 0:
        even_sum += number
        if number < even_min:
            even_min = number
        if number > even_max:
            even_max = number


if n == 0:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")

elif n == 1:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')

else:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')

