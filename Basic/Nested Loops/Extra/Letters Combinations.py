import string

all = string.ascii_lowercase

letter_a = input()
letter_b = input()
letter_c = input()

start_point = all.index(letter_a)
end = all.index(letter_b)
combination = all[start_point: end + 1]
combination = combination.replace(letter_c, '')
combination_number = 0

for first in combination:
    for second in combination:
        for third in combination:
            combination_number += 1
            print(f'{first}{second}{third}', end = ' ')
print(combination_number)
