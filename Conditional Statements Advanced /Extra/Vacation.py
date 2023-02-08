budget = float(input())
season = input()

if budget <= 1000:
    accomodation = 'Camp'
    if season == 'Summer':
        place = 'Alaska'
        budget = .65 * budget
    else:
        place  = 'Morocco'
        budget = .45 * budget

elif 1000 < budget <= 3000 :
    accomodation = 'Hut'
    if season == 'Summer':
        place = 'Alaska'
        budget = .8 * budget
    else:
        place  = 'Morocco'
        budget = .6 * budget

elif budget > 3000 :
    accomodation = 'Hotel'
    if season == 'Summer':
        place = 'Alaska'
        budget = .9 * budget
    else:
        place  = 'Morocco'
        budget = .9 * budget

print(f'{place} - {accomodation} - {budget:.2f}')




