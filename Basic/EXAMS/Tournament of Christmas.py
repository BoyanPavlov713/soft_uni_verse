days = int(input())
total_win = 0
total_money = 0

for day in range(days):
    current_wins = 0
    current_money = 0

    while True:
        sport = input()
        if sport == 'Finish':
            total_win += current_wins
            if current_wins > 0 :
                current_money *= 1.1
                total_money += current_money
                break
        result = input()
        if result == 'win':
            current_wins += 1
            current_money += 20
        elif result == 'lose':
            current_wins -= 1

if total_win > 0:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")




