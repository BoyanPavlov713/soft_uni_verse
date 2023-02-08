bottles = int(input())
input_data = input()
count = 0
pots = 0
plates = 0
tul = 0

given_liquid = bottles * 750

while input_data != 'End':
    count += 1
    input_data = int(input_data)

    if count % 3 == 0:
        pots += input_data
        given_liquid -= input_data * 15

    else:
        plates += input_data
        given_liquid -= input_data * 5
    if given_liquid < 0:
        break
    input_data = input()

diff = abs(given_liquid)
if given_liquid >= 0:
    print("Detergent was enough!")
    print(f'{plates} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {diff} ml.')
else:
    print(f'Not enough detergent, {diff} ml. more necessary!')
