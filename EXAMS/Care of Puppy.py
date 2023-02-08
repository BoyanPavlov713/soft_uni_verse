bought_food = int(input())
input_data = input()
eaten_food = 0
grams_fod = bought_food * 1000


while input_data != 'Adopted':
    input_data = int(input_data)
    eaten_food += input_data

    input_data = input()

diff = abs(grams_fod - eaten_food)
if grams_fod >= eaten_food:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')
