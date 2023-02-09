people = int(input())
nights = int(input())
cards = int(input())
tickets = int(input())
money = nights * 20 + cards * 1.6 + tickets * 6
total = money * people
final = total * 1.25

print(f'{final :.2f}')