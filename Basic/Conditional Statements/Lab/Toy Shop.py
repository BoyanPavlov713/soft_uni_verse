
trip_price = float(input())
number_puzzles: int = int(input())
number_dollies = int(input())
number_tedies = int(input())
number_minions = int(input())
number_lories = int(input())

total_pieces = (number_puzzles + number_dollies + number_tedies +
                number_minions + number_lories)
total_sum = number_puzzles * 2.6 + number_dollies * 3 + number_tedies * 4.1 + number_minions * 8.2 + number_lories * 2
if total_pieces >= 50:
    total_sum = .75 * total_sum
profit = .9 * total_sum
if profit >= trip_price:
   print(f'Yes! {profit - trip_price :.2f} lv left.')
else :
    print(f'Not enough money! {trip_price - profit :.2f} lv needed.')
