saved_money = 0
while True:
    destination = input()
    if destination == 'End':
        break
    cost = float(input())
    saved_money = 0
    while saved_money < cost:
        money = float(input())
        saved_money += money
    print(f'Going to {destination}!')
