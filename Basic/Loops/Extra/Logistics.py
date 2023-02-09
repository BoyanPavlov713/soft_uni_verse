number = int(input())

price_train = 0
price_lorry = 0
price_microbus = 0
total_weight = 0
weight_microbus = 0
weight_lorry = 0
weight_train = 0

for i in range(1,number + 1):
    weight = int(input())
    if weight <= 3:
       price = 200 * weight
       price_microbus += price
       weight_microbus += weight

    elif weight <= 11:
        price = 175 * weight
        price_lorry += price
        weight_lorry += weight

    else:
        price = weight * 120
        price_train += price
        weight_train += weight

total_weight = weight_train + weight_lorry + weight_microbus
total_sum = price_train + price_lorry + price_microbus
average_price = total_sum / total_weight

print(f'{average_price:.2f}')
print(f'{weight_microbus / total_weight * 100:.2f}%')
print(f'{weight_lorry / total_weight * 100:.2f}%')
print(f'{weight_train / total_weight * 100:.2f}%')

