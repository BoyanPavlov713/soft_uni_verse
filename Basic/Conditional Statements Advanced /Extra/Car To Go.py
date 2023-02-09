budget = float(input())
season = input()
if budget <= 100:
    clas = "Economy class"
    if season == 'Summer':
        car = 'Cabrio'
        budget = .35 * budget
    else :
        car ='Jeep'
        budget = .65 * budget
elif 100 <= budget <= 500:
    clas = "Compact class"
    if season == 'Summer':
        car = 'Cabrio'
        budget = .45 * budget
    else:
        car = 'Jeep'
        budget = .8 * budget
elif budget > 500:
    clas = "Luxury class"
    car = 'Jeep'
    budget = .9 * budget

print(f'{clas}')
print(f'{car} - {budget:.2f}')






