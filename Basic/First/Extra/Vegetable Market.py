veggies = float(input())
fruits = float(input())
kg_veggies = int(input())
kg_fruits = int(input())
veg_tot = veggies * kg_veggies / 1.94
fruits_tot = fruits * kg_fruits / 1.94
total = veg_tot + fruits_tot
print(f"{total:.2f}")
