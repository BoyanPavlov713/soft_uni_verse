
hrisantems = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
if season == 'Spring' or season == 'Summer':
    hr_price = 2
    rose_price = 4.1
    tulips_price = 2.5
    if holiday == 'Y':
        hr_price = hr_price * 1.15
        rose_price = rose_price * 1.15
        tulips_price = tulips_price * 1.15
elif season == 'Autumn' or season == 'Winter':
    hr_price = 3.75
    rose_price = 4.5
    tulips_price = 4.15
    if holiday == 'Y':
        hr_price = hr_price * 1.15
        rose_price = rose_price * 1.15
        tulips_price = tulips_price * 1.15
price = hr_price * hrisantems +rose_price * roses + tulips_price * tulips

price = .95 * price
if roses >= 10 and season == 'Winter':
    price = .9 * price
if hrisantems + roses + tulips > 20 :
    price = .8 * price
total = price + 2
print(f'{total:.2f}')