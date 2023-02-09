number_groups = int(input())
total_people = 0
musala_people = 0
montblanc_people = 0
kilimangaro_people = 0
k2_people = 0
everest_people = 0


for i in range(1,number_groups+1):
    number_people_per_group = int(input())
    if number_people_per_group <= 5:
        peak = 'Mussala'
        musala_people += number_people_per_group
    elif number_people_per_group <= 12:
        peak ='Montblanc'
        montblanc_people += number_people_per_group
    elif number_people_per_group <= 25:
        peak = 'Kilimangaro'
        kilimangaro_people += number_people_per_group
    elif number_people_per_group <= 40:
        peak = 'K2'
        k2_people += number_people_per_group
    else:
        peak = 'Everest'
        everest_people += number_people_per_group
    total_people += number_people_per_group

print(f'{musala_people/total_people * 100:.2f}%')
print(f'{montblanc_people/total_people * 100:.2f}%')
print(f'{kilimangaro_people/total_people * 100:.2f}%')
print(f'{k2_people/total_people * 100:.2f}%')
print(f'{everest_people/total_people * 100:.2f}%')


