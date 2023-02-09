input_data = input()

goal = 10000
steps = 0
total = 0

while input_data != 'Going home':
    steps = int(input_data)
    total += steps
    if total >= 10000:
        break

    input_data = input()

if input_data == 'Going home':
    home_steps = int(input())
    total += home_steps
diff = abs(total - goal)
if total >= goal:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')

