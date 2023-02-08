n = int(input())
total = 0

for _ in range(n):
    litters = int(input())
    if total + litters > 255:
        print("Insufficient capacity!")
    else:
        total += litters

print(total)
