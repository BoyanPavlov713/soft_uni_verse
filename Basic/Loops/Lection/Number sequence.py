import sys

n = int(input())
max_num = - sys.maxsize
min_number = sys.maxsize

for i in range(n):
    current_num = int(input())

    if current_num > max_num:
        max_num = current_num
    if current_num < min_number:
        min_number = current_num

print(f'Max number: {max_num}')
print(f'Min number: {min_number}')

