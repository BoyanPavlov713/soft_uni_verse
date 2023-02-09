num = str(input())
for first_num in range(1, int(num[2]) + 1):
    for second_num in range(1, int(num[1]) + 1):
        for third_num in range(1, int(num[0]) + 1):
            total = first_num * second_num * third_num
            print(f'{first_num} * {second_num} * {third_num} = {total};')


