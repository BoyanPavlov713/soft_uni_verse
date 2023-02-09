import math
days = int(input())
total_food = float(input())
n = 1
total_dog_food = 0
total_cat_food = 0
total_bisquites = 0

while n <= days:
    dog_food = int(input())
    cat_food = int(input())
    total_dog_food += dog_food
    total_cat_food += cat_food
    if n % 3 == 0:
        bisquites = .1 *(dog_food + cat_food)
        total_bisquites += bisquites
    n += 1

food = total_dog_food + total_cat_food

print(f'Total eaten biscuits: {round(total_bisquites)}gr.')
print(f'{food/total_food *100:.2f}% of the food has been eaten.')
print(f'{total_dog_food / food *100:.2f}% eaten from the dog.')
print(f'{total_cat_food / food *100:.2f}% eaten from the cat.')
