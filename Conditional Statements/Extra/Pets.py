days = int(input())
total_food = int(input())
dog_food_day = float(input())
cat_food_day = float(input())
turtle_food_day_grams = float(input())
import math

food_needed = days*(dog_food_day + cat_food_day + turtle_food_day_grams/1000)
if total_food >= food_needed :
    print(f"{ math.floor(total_food - food_needed)} kilos of food left.")
elif total_food < food_needed :
    print(f"{math.ceil(food_needed - total_food)} more kilos of food are needed.")