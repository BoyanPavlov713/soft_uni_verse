
days = int(input())
sport = input()
win = 0
lose = 0
total_win = 0
total_loss = 0
total_money = 0

for n in range(1, days+1):
     if sport == 'Finish':
         break
     sport = input()
     while sport != 'Finish':
        result = input()
        if result == 'win':
            win += 1
            total_money = win * 20
        elif result == 'lose':
            lose +=1
        sport = input()
        if win > lose:
            total_money = 1.1 * total_money

if total_win > total_loss:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
