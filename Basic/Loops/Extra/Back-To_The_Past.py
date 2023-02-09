inherited_money = float(input())
year_of_death = int(input())
age = 18
spent_money = 0
for i in range(1800,year_of_death+1):
    if i % 2 == 0:
        spend_yearly = 12000
    else:
        spend_yearly = 12000 + (age + i - 1800) * 50

    spent_money += spend_yearly
if inherited_money >= spent_money:
    print(f'Yes! He will live a carefree life and will have {inherited_money - spent_money:.2f} dollars left.')
else:
    print(f'He will need {spent_money - inherited_money:.2f} dollars to survive.')

