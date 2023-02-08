lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

money = 0

for i in range(1, lost_fights + 1):

    if i % 2 == 0:
        money += helmet
    if i % 3 == 0:
        money += sword
    if i % 6 == 0:
        money += shield
    if i % 12 == 0:
        money += armor

print(f"Gladiator expenses: {money:.2f} aureus")