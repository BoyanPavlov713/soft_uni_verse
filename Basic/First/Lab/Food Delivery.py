chicken = int(input())
fish = int(input())
veg = int(input())
chicken_sum = chicken * 10.35
fish_sum = fish * 12.40
veg_sum = veg * 8.15
dessert = (chicken_sum + fish_sum + veg_sum) * 0.20
all_sum = (chicken_sum + fish_sum + veg_sum) + dessert + 2.5
print(all_sum)
