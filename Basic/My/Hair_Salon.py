gain = int(input())

is_not_reached = True
total_price = 0

while True:
    service = input()
    if service == 'closed':
        if gain > total_price:
            print(f"Target not reached! You need {gain - total_price}lv. more.")
        elif gain <= total_price:
            print(f"You have reached your target for the day!")
        is_not_reached = False
        break

    if service == 'haircut':
        gender = input()
        if gender == 'mens':
            price = 15
        elif gender == 'ladies':
            price = 20
        elif gender == 'kids':
            price = 10

    elif service == 'color':
        type = input()
        if type == 'touch up':
            price = 20
        elif type == 'full color':
            price = 30

    total_price += price

    if total_price >= gain:
        print(f"You have reached your target for the day!")
        is_not_reached = False
        break

print(f"Earned money: {total_price}lv.")