budget = float(input())
season = input()
price = 0
if budget <= 100:
    if season == 'summer':
        price = budget * .3
        room = 'Camp'
    elif season == 'winter':
        price = .7 * budget
        room = 'Hotel'
    place = 'Bulgaria'

elif budget <= 1000 :
    if season == 'summer':
        price = .4 * budget
        room = 'Camp'
    elif season == 'winter':
        price = .8 * budget
        room = 'Hotel'
    place = 'Balkans'

elif budget > 1000:
    price = .9 * budget
    place = 'Europe'
    room = 'Hotel'

print(f'Somewhere in {place}')
print(f'{room} - {price:.2f}')

