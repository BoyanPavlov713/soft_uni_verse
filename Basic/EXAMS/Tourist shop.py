budget = float(input())
total = 0
number_products = 0
needed_money = 0
cost = 0
budget_condition = False

while True:
    name_product = input()

    if name_product == 'Stop':
        break

    price_product = float(input())
    number_products += 1

    if number_products % 3 == 0:
        price_product /= 2
    if price_product > budget:
        budget_condition = True
        needed_money = price_product - budget
        number_products -= 1
        break

    budget -= price_product
    cost += price_product
if not budget_condition:
    print(f"You bought {number_products} products for {cost:.2f} leva.")
else:
    print(f"You don't have enough money!")
    print(f"You need {needed_money:.2f} leva!")
