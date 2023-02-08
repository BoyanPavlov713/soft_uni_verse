size = int(input())
days = int(input())
coins = 0


for day in range(1,days + 1):
    if day % 10 == 0:
        size -= 2
    if day % 15 == 0:
        size += 5
        coins -= 2 * size

    coins += 50 - 2 * size

    if day % 3 == 0:
        coins -= 3 * size
    if day % 5 == 0:
        coins += 20 * size

coins_per_capita = coins // size

print(f"{size} companions received {coins_per_capita} coins each.")