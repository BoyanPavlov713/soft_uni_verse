start_number = int(input())
end_number = int(input())

for number in range(start_number, end_number +1):

    hundreds_thousends = number // 100000
    ten_thousends = (number // 10000) % 10
    thousends = (number // 1000) % 10
    hundreds = (number // 100) % 10
    tens =(number // 10) % 10
    units = number % 10

    sum_even = ten_thousends + hundreds + units
    sum_odd = hundreds_thousends + thousends + tens
    if sum_even == sum_odd:
        print(number, end = ' ')