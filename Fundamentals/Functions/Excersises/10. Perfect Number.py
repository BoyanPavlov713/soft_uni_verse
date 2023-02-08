def proper_func(some_number):
    counter = 0
    for num in range(1, some_number):
        if some_number % num == 0:
            counter += num
    if counter == some_number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
    return


number = int(input())
proper_func(number)


