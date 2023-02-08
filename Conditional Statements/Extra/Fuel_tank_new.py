fuel = input()
litres = float(input())

if fuel == 'Gas' or fuel == 'Diesel' or fuel == 'Gasoline':
    if litres >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
else:
    print("Invalid fuel!")