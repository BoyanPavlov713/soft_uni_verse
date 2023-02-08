num = int(input())
total = 0

for i in range(1, num + 1):
    if i <= num:
        current_number = int(input())

    total += current_number


print(f'{total / num :.2f}')
