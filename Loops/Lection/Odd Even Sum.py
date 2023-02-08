n = int(input())
number = 0
odd_sum = 0
even_sum = 0


for i in range(1,n + 1):
    current_number = int(input())
    number +=1
    if number % 2 != 0:
        odd_sum = odd_sum + current_number
    else:
        even_sum = even_sum + current_number
if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {odd_sum}')
else:
    diff = abs(odd_sum - even_sum)
    print('No')
    print(f'Diff = {diff}')



