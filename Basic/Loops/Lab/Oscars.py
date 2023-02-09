name_actor = input()
points =float(input())
number = int(input())

total_points = points

for i in range(1, number + 1):
    name = input()
    number_points = float(input())

    person_points = (len(name) * number_points) / 2
    total_points = total_points + person_points

    if total_points >= 1250.5:
        break

if total_points < 1250.5:
    print(f'Sorry, {name_actor} you need {1250.5 - total_points:.1f} more!')
else:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!')
