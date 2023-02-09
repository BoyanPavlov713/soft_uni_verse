
season = input()
type_group = input()
number_pupils = int(input())
number_nights = int(input())
price_night = 0

if season == 'Winter':
    if type_group == 'girls':
        price_night = 9.60
        sport = 'Gymnastics'
    elif type_group == 'boys':
        price_night = 9.60
        sport = 'Judo'
    elif type_group == 'mixed':
        price_night = 10
        sport = 'Ski'


elif season == 'Spring':
    if type_group == 'girls':
        price_night = 7.2
        sport = 'Athletics'
    elif type_group == 'boys':
        price_night = 7.2
        sport = 'Tennis'
    elif type_group == 'mixed':
        price_night = 9.5
        sport = 'Cycling'


elif season == 'Summer':
    if type_group == 'girls':
        price_night = 15
        sport = 'Volleyball'
    elif type_group == 'boys':
        price_night = 15
        sport = 'Football'
    elif type_group == 'mixed':
        price_night = 20
        sport = 'Swimming'


if number_pupils >= 50:
    price_night = price_night *.5
elif 20 <= number_pupils < 50:
    price_night = .85 * price_night
elif 10 <= number_pupils < 20:
    price_night = .95 * price_night

total = price_night * number_nights * number_pupils
print(f'{sport} {total:.2f} lv.')


