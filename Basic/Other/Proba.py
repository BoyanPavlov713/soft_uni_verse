

cost = 0
spirit = 0

decs_per_time = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15



for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        decs_per_time += 2
    if current_day % 2 == 0:
        cost += ornament_set * decs_per_time
        spirit += 5

    if current_day % 3 == 0:
        cost += (tree_skirt + tree_garlands) * decs_per_time
        spirit += (3 + 10)

    if current_day % 5 == 0:
        cost += tree_lights * decs_per_time
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30

    if current_day % 10 == 0:
        spirit -= 20
        cost += (tree_skirt + tree_garlands + tree_lights)



if days % 10 == 0:
    spirit -= 30

print(f'Total cost: {cost}')
print(f'Total spirit: {spirit}')


