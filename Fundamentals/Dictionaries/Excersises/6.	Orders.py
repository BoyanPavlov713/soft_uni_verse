price_product = {}
qhnt_product = {}

while True:
    data = input()
    if data == 'buy':
        break
    args = data.split()
    type_drink = args[0]
    price_drink = float(args[1])
    qnt_drink = float(args[2])

    if type_drink in price_product:
        price_product[type_drink] = price_drink
        qhnt_product[type_drink] += qnt_drink
    else:
        price_product[type_drink] = price_drink
        qhnt_product[type_drink] = qnt_drink
for type_drink in price_product:
    print(f'{type_drink} -> {(qhnt_product[type_drink] * price_product[type_drink]):.02f}')
