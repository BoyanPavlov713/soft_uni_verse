x = float(input())
y = float(input())
h = float(input())
green_walls = (2*x + 2*y) * x -2.4 - 3*1.5
red_roof = 2* x * y +x * h
green = green_walls / 3.4
red = red_roof / 4.3
total = green + red
print(f"{green:.2f}")
print(f"{red:.2f}")
