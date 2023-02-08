import sys
n = int(input())
total_sum = 0
max_number = - sys.maxsize


for i in range(n):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number
    total_sum = total_sum + current_number

if total_sum - max_number == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    sum_others = total_sum - max_number
    print(f'Diff = {abs(max_number - sum_others)}')



