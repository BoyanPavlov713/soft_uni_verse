flower = input()
number_flowers = int(input())
budget = int(input())
price = 0


if flower == 'Roses' :
    price = 5
elif flower == 'Dahlias' :
    price = 3.8
elif flower == 'Tulips' :
    price = 2.80
elif flower == 'Narcissus' :
    price = 3
elif flower == 'Gladiolus' :
    price = 2.5


if flower == 'Roses' and number_flowers > 80:
    price = .9 * price
elif flower == 'Dahlias' and number_flowers > 90:
    price = .85 * price
elif flower == 'Tulips' and number_flowers > 80:
    price = .85 * price
elif flower == 'Narcissus' and number_flowers < 120:
    price = 1.15 * price
elif flower == 'Gladiolus' and number_flowers < 80:
    price = 1.2 * price
total_price = price * number_flowers

diff = abs(budget - total_price)
if budget >= total_price:
    print(f'Hey, you have a great garden with {number_flowers} {flower} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')