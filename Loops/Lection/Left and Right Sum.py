n = int(input())
number = 0
total_sum = 0
left_sum = 0
right_sum = 0

for i in range(1,(2 * n)+1):
    current_number = int(input())
    number += 1
    total_sum = total_sum + current_number

    if number <= n:
        left_sum = left_sum + current_number

    elif number > n:
        right_sum = total_sum - left_sum

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {diff}')







