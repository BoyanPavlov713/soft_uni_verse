from math import pi
type = input()
if type == "square" :
    a = float(input())
    area = a**2
    print(f'{area :.3f}')
if type == "rectangle" :
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area :.3f}')
if type == "triangle" :
    a = float(input())
    b = float(input())
    area = a * b /2
    print(f'{area :.3f}')
if type == "circle" :
    a = float(input())
    area = pi * a**2
    print(f'{area :.3f}')






