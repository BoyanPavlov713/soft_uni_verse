num = int(input('Enter a number between10 and 20: '))

while num < 10 or num > 20:
    if num < 10:
        print('Too low, please try again!')
    elif num > 20:
        print('Too high,please try again!')
    num = int(input('Enter a number between10 and 20: '))
print('Thank you!')
