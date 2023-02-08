a = int(input())
b = int(input())
c = int(input())
prime_numbers = [2,3,5,7]
for first in range(1, a + 1):
    if first % 2 == 0:
        for second in range(1, b +1):
            if second in prime_numbers:
                for third in range(1, c + 1):
                    if third % 2 == 0:
                        print(f'{first} {second} {third}')


