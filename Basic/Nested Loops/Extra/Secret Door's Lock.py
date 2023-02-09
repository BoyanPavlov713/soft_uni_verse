hundreds = int(input())
tens = int(input())
units = int(input())

prime_numbers = [2,3,5,7]

for num1 in range(1,hundreds +1):
    for num2 in range(1,tens +1):
        for num3 in range(1,units +1):
            if num1 % 2 == 0 and num3 % 2 == 0:
                if num2 in prime_numbers:
                    print(f'{num1} {num2} {num3}')
