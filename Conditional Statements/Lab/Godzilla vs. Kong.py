budget = float(input())
number_people = int(input())
clothing_per_person = float(input())
decor = .1 * budget
cost = number_people * clothing_per_person + decor
if number_people > 150 :
    cost = number_people*clothing_per_person * .9 + decor
if  budget < cost:
    print("Not enough money!")
    print(f"Wingard needs {cost - budget :.2f} leva more.")
else:
    print("Action!" )
    print(f"Wingard starts filming with {budget - cost:.2f} leva left.")
