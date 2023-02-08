
total = 0
while True:
    money = input()
    if money == 'NoMoreMoney':
        break
    money = float(money)

    if money < 0:
         print("Invalid operation!")
         break

    print(f'Increase: {money:.2f}')
    total += money


print(f'Total: {total:.2f}')