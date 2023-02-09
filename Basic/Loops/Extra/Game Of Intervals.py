moves = int(input())

points = 0
total_points = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0

for i in range(1, moves + 1):
    number = int(input())

    if 0 <= number < 10:
        points = .2 * number
        count_1 += 1
        total_points += points
    elif 10 <= number < 20:
        points = .3 * number
        count_2 += 1
        total_points += points
    elif 20 <= number < 30:
        points = .4 * number
        count_3 += 1
        total_points += points
    elif 30 <= number < 40:
        points = 50
        count_4 += 1
        total_points += 50
    elif 40 <= number <= 50:
        points = 100
        count_5 += 1
        total_points += 100
    else:
        total_points /= 2
        count_6 += 1


print(f'{total_points:.2f}')
print(f'From 0 to 9: {count_1 / moves * 100:.2f}%')
print(f'From 10 to 19: {count_2 / moves * 100:.2f}%')
print(f'From 20 to 29: {count_3 / moves * 100:.2f}%')
print(f'From 30 to 39: {count_4 / moves * 100:.2f}%')
print(f'From 40 to 50: {count_5 / moves * 100:.2f}%')
print(f'Invalid numbers: {count_6 / moves * 100:.2f}%')




