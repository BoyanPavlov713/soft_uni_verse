age = int(input())
price = float(input())
toy_price = int(input())

money = 0
saved_money = 0
toys = 0
brother = 0

for i in range(1,age+1):
    if i % 2 == 0:
        money += 10
        saved_money = saved_money + money
        brother += 1
    else:
        toys += 1
total = saved_money + (toys * toy_price) - brother
if total >= price:
    print(f'Yes! {total - price:.2f}')
else:
    print(f'No! {price - total:.2f}')




