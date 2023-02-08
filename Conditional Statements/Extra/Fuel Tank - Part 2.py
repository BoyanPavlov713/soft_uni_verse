fuel = input()
litres = float(input())
discount = input()
price = 0


if fuel == "Gas" :
    if discount == "No":
       price = .93 * litres
    elif discount == "Yes" :
       price = .85 * litres

    if 20 < litres <= 25 :
        price = .92 * price

    elif 25 < litres :
        price = .9 * price
    print(f'{price :.2f} lv. ')


if fuel == "Gasoline" :
    if discount == "No":
       price = 2.22 * litres
    elif discount == "Yes" :
       price = 2.04 * litres

    if 20 < litres <= 25 :
        price = .92 * price

    elif 25 < litres :
        price = .9 * price
    print(f'{price :.2f} lv. ')


if fuel == "Diesel" :
    if discount == "No":
       price = 2.33 * litres
    elif discount == "Yes" :
       price = 2.21 * litres

    if 20 < litres <= 25 :
        price = .92 * price

    elif 25 < litres :
        price = .9 * price
    print(f'{price :.2f} lv. ')








