
fruit = input()
size = input()
numbers = int(input())
price_per_unit = 0
price_per_box = 0

if fruit == 'Watermelon':
    if size == "small":
        price_per_unit = 56
    elif size == 'big':
        price_per_unit = 28.7
elif fruit == "Mango" :
    if size == "small":
        price_per_unit = 36.66
    elif size == 'big':
        price_per_unit = 19.6
elif fruit == "Pineapple":
    if size == "small":
            price_per_unit = 42.1
    elif size == 'big':
            price_per_unit = 24.8
elif fruit == "Raspberry":
    if size == "small":
            price_per_unit = 20
    elif size == 'big':
            price_per_unit = 15.2
if size == "small":
    price_per_box = 2 * price_per_unit
else:
    price_per_box = 5 * price_per_unit

total = numbers * price_per_box
if 400 <= total <= 1000:
    total = .85 * total
elif total > 1000:
    total = .5 * total

print(f'{total:.2f} lv.')




