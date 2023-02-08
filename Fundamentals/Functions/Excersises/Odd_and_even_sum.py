def even_odd_sum(digits_as_str):

    even = 0
    odd = 0
    for digit_as_string in digits_as_str:
        digit = int(digit_as_string)

        if digit % 2 == 0:
            even += digit
        else:
            odd += digit
    return f"Odd sum = {odd}, Even sum = {even}"


num_as_str = input()
print(even_odd_sum(num_as_str))