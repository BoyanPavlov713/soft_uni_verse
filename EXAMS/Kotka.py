number_days = int(input())
number_hours = int(input())
total_cost = 0

for day in range(1, number_days + 1):
    current_cost = 0
    for hour in range(1, number_hours +1):
        if day % 2 == 0 and hour % 2 == 0 :
            current_cost += 2.5
            total_cost += 2.5
        elif day % 2 != 0 and hour % 2 != 0:
            current_cost += 1.25
            total_cost +=1.25
        else:
            current_cost += 1
            total_cost += 1
    print(f"Day: {day} – {current_cost} leva")

print(f"Total: {total_cost} leva")
