bitkoins = int(input())
chine = float(input())
commission = float(input())
money = (bitkoins * 1168 + chine * .15 * 1.76) / 1.95
total = money - money * commission / 100
print(f'{total:.2f}')
