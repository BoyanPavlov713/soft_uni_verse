h = int(input())
w = int(input())
windows = int(input())

used_paint = 0
square = h * w * 4
needed_paint = square -  (windows * square / 100)
not_painted = True
while True:
    paint = input()

    if paint == 'Tired!':
        print(f"{needed_paint} quadratic m left.")
        not_painted = False
    else:
        paint = int(paint)
        needed_paint -= paint

    if needed_paint < 0:
        print(f"All walls are painted and you have {needed_paint} l paint left!")
        not_painted = False
    elif needed_paint == 0:
        print(f"All walls are painted! Great job, Pesho!" )
        not_painted = False



