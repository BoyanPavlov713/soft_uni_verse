price = float(input())
initial_money = float(input())

days = 0
shopping = 0

while initial_money < price and shopping < 5:
    action = input()
    moneys = float(input())
    days += 1

    if action == 'save':
        initial_money += moneys
        shopping = 0
    elif action == 'spend':
        initial_money -= moneys
        shopping += 1
        if initial_money < 0:
            initial_money = 0

if shopping == 5:
    print("You can't save the money.")
    print(days)
if initial_money >= price:
    print(f'You saved the money for {days} days.')






