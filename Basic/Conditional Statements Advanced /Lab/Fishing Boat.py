budget = int(input())
season = input()
number_people = int(input())
price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
   price = 4200
elif season == 'Winter':
    price = 2600
if number_people <= 6:
   price = .9 * price
elif 7 <= number_people <= 11:
   price = price * .85
elif number_people >= 12:
    price = .75 * price

if number_people % 2 == 0 and season != 'Autumn':
    price = .95 * price

if budget >= price:
    print(f'Yes! You have {budget - price:.2f} leva left.')
else:
    print(f'Not enough money! You need {price - budget:.2f} leva.')

