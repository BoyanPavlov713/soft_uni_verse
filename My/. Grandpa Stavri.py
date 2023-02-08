days = int(input())
total_litters = 0
strongness = 0

for a in range(1,days+1):
    litters = float(input())
    gradus = float(input())

    total_litters += litters
    strongness += litters * gradus
    degrees = strongness / total_litters

print(f"Liter: {total_litters:.2f}")
print(f"Degrees: {degrees:.2f}")

average = strongness / total_litters

if average < 38:
    print(f"Not good, you should baking!")
elif 38 <= average <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")