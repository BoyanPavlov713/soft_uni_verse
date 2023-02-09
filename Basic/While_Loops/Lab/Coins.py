amount = float(input())
coins_amount = amount * 100
count_coins = 0

while coins_amount > 0:
    if coins_amount >= 200:
        coins_amount -= 200
        count_coins += 1
    elif coins_amount >= 100:
         coins_amount -= 100
         count_coins += 1
    elif coins_amount >= 50:
         coins_amount -= 50
         count_coins += 1
    elif coins_amount >= 20:
         coins_amount -= 20
         count_coins += 1
    elif coins_amount >= 10:
         coins_amount -= 10
         count_coins += 1
    elif coins_amount >= 5:
         coins_amount -= 5
         count_coins += 1
    elif coins_amount >= 2:
         coins_amount -= 2
         count_coins += 1
    elif coins_amount >= 1:
         coins_amount -= 1
         count_coins += 1
    else:
        break

print(count_coins)