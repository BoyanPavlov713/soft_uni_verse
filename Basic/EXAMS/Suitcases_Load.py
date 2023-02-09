volume = float(input())
suitcase_volume = input()
total_volume = 0
suitcases = 0

while suitcase_volume != "End":
    suitcase_volume = float(suitcase_volume)
    suitcases += 1
    if suitcases % 3 == 0:
        suitcase_volume = 1.1 * suitcase_volume
    volume -= suitcase_volume
    if volume < 0:
        suitcases -= 1
        break

    suitcase_volume = input()


if volume >= total_volume:
    print('Congratulations! All suitcases are loaded!')
else:
    print("No more space!")

print(f'Statistic: {suitcases} suitcases loaded.')


