import math
radius = int(input('Enter the radius: '))
depth = int(input('Enter the depth: '))
circle_area = math.pi * (radius**2)
volume = depth * circle_area
print(round(volume,3))