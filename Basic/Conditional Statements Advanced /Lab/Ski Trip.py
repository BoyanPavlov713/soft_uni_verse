days = int(input())
type_room = input()
score = input()
nights = days - 1
price = 0


if type_room == "room for one person":
    price = 18

elif type_room =="apartment":
    price = 25
    if days < 10 :
        price = .7 * price
    elif 10 <=days <= 15:
        price = .65 * price
    else:
        price = .5 * price

elif type_room == "president apartment":
    price = 35
    if days < 10 :
        price = .9 * price
    elif 10 <=days <= 15:
        price = .85 * price
    else:
        price = .8 * price

if score == 'positive':
    price = 1.25 * price
else:
    price = .9 * price

total_price = nights * price

print(f'{total_price:.2f}')


