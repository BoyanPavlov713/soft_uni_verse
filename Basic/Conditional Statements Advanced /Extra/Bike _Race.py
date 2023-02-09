junior_number = int(input())
senior_number = int(input())
track = input()
if track == 'trail':
    summ = junior_number * 5.5 + senior_number * 7
elif track == 'cross-country':
    summ = junior_number * 8 + senior_number * 9.5
    if (junior_number + senior_number) >= 50:
        summ =.75 * summ
elif track == 'downhill':
    summ = junior_number * 12.25 + senior_number * 13.75
elif track == 'road':
    summ = junior_number * 20 + senior_number * 21.5


leftover = .95 * summ
print(f'{leftover:.2f}')

