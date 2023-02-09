sold_games = int(input())
total_Hearthstone= 0
total_Fornite = 0
total_Overwatch = 0
total_Others = 0

for i in range(1,sold_games +1):
    game = input()

    if game == 'Hearthstone':
        total_Hearthstone += 1
    elif game == 'Fornite':
        total_Fornite += 1
    elif game == 'Overwatch':
        total_Overwatch += 1
    else:
        total_Others += 1

total_sells = total_Hearthstone + total_Overwatch + total_Fornite + total_Others

print(f'Hearthstone - {total_Hearthstone / total_sells *100:.2f}%')
print(f'Fornite - {total_Fornite / total_sells * 100:.2f}%')
print(f'Overwatch - {total_Overwatch / total_sells * 100:.2f}%')
print(f'Others - {total_Others / total_sells * 100:.2f}%')