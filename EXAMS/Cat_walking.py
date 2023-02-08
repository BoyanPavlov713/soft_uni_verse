minutes = int(input())
count_walks = int(input())
calories = int(input())
total_walk = minutes * count_walks
total_calories = total_walk * 5
if total_calories >= .5 * calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_calories}.')