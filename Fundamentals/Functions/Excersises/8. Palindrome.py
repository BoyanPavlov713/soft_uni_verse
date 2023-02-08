def palindrome_func(numbers):
    for num in numbers:
        if num == num[::-1]:
            print(True)
        else:
            print(False)


numbers = input().split(', ')
palindrome_func(numbers)
