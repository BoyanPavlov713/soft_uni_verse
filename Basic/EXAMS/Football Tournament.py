name = input()
number_games = int(input())
total_points = 0
games_played = 0
w =0
d = 0
l = 0
flag = True
for result in range(1, number_games + 1):
    result = input()

    if number_games == 0:
        flag = False
        break
    if result == 'W':
        w +=1
        total_points += 3
    elif result == 'D':
        total_points += 1
        d += 1
    elif result == 'L':
        l += 1
        total_points += 0
    games_played += 1
if  flag:
        win_rate = w / games_played * 100
        print(f"{name} has won {total_points} points during this season")
        print("Total stats:")
        print(f"## W: {w}")
        print(f"## D: {d}")
        print(f"## L: {l}")
        print(f'Win rate: {win_rate:.2f}')
else:
    print(f"{name} hasn't played any games during this season.")

