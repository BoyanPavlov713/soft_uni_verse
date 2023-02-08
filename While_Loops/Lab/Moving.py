w = int(input())
length = int(input())
h = int(input())
volume = w * length * h
total = 0

input_boxes = input()
while input_boxes != 'Done':
    input_boxes = int(input_boxes)
    total += input_boxes
    if total >= volume:
        break

    input_boxes = input()

diff = abs(total - volume)

if volume > total:
    print(f'{diff} Cubic meters left.')
else:
    print(f"No more free space! You need {diff} Cubic meters more.")