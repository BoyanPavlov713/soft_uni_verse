
import math
number_tournament = int(input())
stage = int(input())
count_w = 0
count_f = 0
count_sf = 0

for i in range(1, number_tournament + 1):
    init_points = input()
    if init_points == 'W':
        count_w += 1
    elif init_points == 'F':
        count_f += 1
    elif init_points == 'SF':
        count_sf += 1


total_points = count_w * 2000 + count_f * 1200 + count_sf * 720 + stage
print(f'Final points: {total_points}')
print(f'Average points: {math.floor((total_points - stage)/ number_tournament)}')
print(f'{(count_w / number_tournament) * 100:.2f}%')