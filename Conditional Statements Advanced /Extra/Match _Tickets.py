budget = float(input())
category = input()
number_people = int(input())
transport = 0

if category == 'Normal':
    if 1 <= number_people <= 4:
        transport = .75 * budget
    elif 5 <= number_people <= 9:
        transport = .6 * budget
    elif 10 <= number_people <= 24:
        transport = .5 * budget
    elif 25 <=number_people <= 49:
        transport = .4 * budget
    else :
        transport = .25 * budget
    cost = number_people * 249.99


elif category == 'VIP':
    if 1 <= number_people <= 4:
        transport = .75 * budget
    elif 5 <= number_people <=9:
        transport = .6 * budget
    elif 10 <= number_people <= 24:
        transport = .5 * budget
    elif 25 <= number_people <= 49:
        transport = .4 * budget
    else:
        transport = .25 * budget

    cost = number_people * 499.99
leftover = budget - transport - cost

if leftover >= 0:
    print(f'Yes! You have {abs(leftover) :.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(leftover ) :.2f} leva.')