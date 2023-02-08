season = input()
km_monthly = float(input())

if km_monthly <= 5000 :
    if 'Spring' == season or season == 'Autumn':
        money = km_monthly * .75 *4
    elif season == 'Summer':
        money = km_monthly * .9 * 4
    elif season == 'Winter':
        money = km_monthly * 1.05 * 4

elif 5000 < km_monthly <= 10000:
    if 'Spring' == season  or season == 'Autumn':
        money = km_monthly * .95 * 4
    elif season == 'Summer':
        money = km_monthly * 1.1 * 4
    elif season == 'Winter':
        money = km_monthly * 1.25 * 4

elif 10000 < km_monthly <= 20000:
    money = km_monthly * 1.45 * 4

profit_after_tax = money * .9

print(f'{profit_after_tax:.2f}')




