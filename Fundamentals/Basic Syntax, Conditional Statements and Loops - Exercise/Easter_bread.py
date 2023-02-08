budget = float(input())
flour_price = float(input())

egg_price = .75 * flour_price
milk_price = 1.25 * flour_price / 4
bread_price = flour_price + egg_price + milk_price
number_bread = 0
coloured_eggs = 0

while budget > bread_price:
    number_bread += 1
    budget -= bread_price
    coloured_eggs += 3
    if number_bread % 3 == 0:
        coloured_eggs -= number_bread - 2
print(f"You made {number_bread} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.02f}BGN left.")




