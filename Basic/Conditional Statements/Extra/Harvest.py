import math
x_sqm = int(input())
y_kg = float(input())
z_liters =(int(input()))
workers = int(input())

wine_total = (0.4 * x_sqm * y_kg / 2.5)
lacks = abs(wine_total - z_liters)

if wine_total < z_liters:
    print(f"It will be a tough winter! More {math.floor(lacks)} liters wine needed.")
elif wine_total >= z_liters:
     print(f"Good harvest this year! Total wine: {math.floor(wine_total):.0f} liters.")
     print(f"{math.ceil(lacks)} liters left -> {math.ceil(lacks / workers)} liters per person.")
