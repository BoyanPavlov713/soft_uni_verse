month = input()
number_nights = int(input())
if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
elif month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.7
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

if 14 >= number_nights > 7 and (month == 'May' or month == 'October'):
    studio_price =.95 * studio_price
elif number_nights > 14 and (month == 'May' or month == 'October'):
    studio_price =.7 * studio_price
elif number_nights > 14 and (month == 'June' or month == 'September'):
    studio_price =.8 * studio_price

if number_nights >14 :
    apartment_price = .9 * apartment_price

print(f'Apartment: {apartment_price * number_nights:.2f} lv.')
print(f'Studio: {studio_price * number_nights:.2f} lv.')




