weigth = float(input())
service = input()
distance = int(input())

if service == 'standard':
    if weigth < 1:
        price = 3 * distance
    elif 1 <= weigth < 10:
        price = 5 * distance
    elif 10 <= weigth < 40:
        price = 10 * distance
    elif 40 <= weigth < 90:
        price = 15 * distance
    elif 90 <= weigth <= 150:
        price = 20 * distance

elif service == 'express':
    if weigth < 1:
        price = 3 * distance + 3 * distance * weigth * 80 / 100
    if 1 <= weigth < 10:
        price = 5 * distance + 5 * distance * weigth * 40 / 100
    elif 10 <= weigth < 40:
        price = 10 * distance + 10 * distance * weigth * 5 / 100
    elif 40 <= weigth < 90:
        price = 15 * distance + 15 * distance * weigth * 2 / 100
    elif 90 <= weigth <= 150:
        price = 20 * distance + 20 * distance * weigth * 1 / 100


print(f"The delivery of your shipment with weight of {weigth:.3f} kg. would cost {price / 100:.2f} lv.")