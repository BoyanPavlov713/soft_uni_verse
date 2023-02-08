budget = float(input())
videocards = int(input())
processors = int(input())
ram = int(input())
cost = videocards * 250 + processors * videocards *250 * .35 + ram * videocards * 250 * .1
if videocards > processors :
    cost = .85 * cost
if budget >= cost :
    print(f'You have {budget - cost:.2f} leva left!')
else:
    print(f'Not enough money! You need {cost - budget:.2f} leva more!')


