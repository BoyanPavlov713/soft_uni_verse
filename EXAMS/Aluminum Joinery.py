number_joinery = int(input())
type = input()
delivery = input()
price = 0
total_prie = 0
flag = True

if number_joinery < 10:
    flag = False
else:
    if type == "90X130":
        if number_joinery > 60:
            price = 110 * .92
        elif number_joinery > 30:
            price = 110 * .95
        elif number_joinery > 10:
            price = 110
    elif type == '100X150':
        if number_joinery > 80:
            price = 140 * .9
        elif number_joinery > 40:
            price = 140 * .94
        elif number_joinery > 10:
            price = 140
    elif type == "130X180":
        if number_joinery > 50:
            price = 190 * .88
        elif number_joinery > 20:
            price = 190 * .93
        elif number_joinery > 10:
            price = 190
    elif type == "130X180":
        if number_joinery > 50:
            price = 250 * .86
        elif number_joinery > 25:
            price = 250 * .91
        elif number_joinery > 10:
            price = 250

total_price = price * number_joinery
if delivery == "With delivery":
    total_price += 60
if number_joinery > 99:
    total_price *= .96

if not flag:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")
