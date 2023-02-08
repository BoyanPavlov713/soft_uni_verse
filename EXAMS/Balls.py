number_balls = int(input())

Total_points = 0
Red_balls = 0
Orange_balls = 0
Yellow_balls = 0
White_balls = 0
Other_colors_picked = 0
divides_from_black_balls = 0

for ball in range(1, number_balls + 1):
    ball = input()
    if ball == 'red':
        Red_balls += 1
        Total_points += 5
    elif ball == 'orange':
        Orange_balls += 1
        Total_points += 10
    elif ball == 'yellow':
        Yellow_balls += 1
        Total_points += 15
    elif ball == 'white':
        White_balls += 1
        Total_points += 20
    elif ball == 'black':
        divides_from_black_balls += 1
        Total_points = int(Total_points / 2)
    else:
        Other_colors_picked += 1

print(f'Total points: {Total_points}')
print(f"Red balls: {Red_balls}")
print(f"Orange balls: {Orange_balls}")
print(f"Yellow balls: {Yellow_balls}")
print(f"White balls: {White_balls}")
print(f"Other colors picked: {Other_colors_picked}")
print(f"Divides from black balls: {divides_from_black_balls}")



