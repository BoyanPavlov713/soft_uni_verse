groups = int(input())
total_Mussala = 0
total_Montblanc = 0
total_Kilimangaro = 0
total_K2 = 0
total_Everest = 0
total_people = 0

for n in range(groups):
  people_per_group = int(input())

  if people_per_group <= 5:
        total_Mussala += people_per_group
  elif people_per_group <= 12:
        total_Montblanc += people_per_group
  elif people_per_group <= 25:
        total_Kilimangaro += people_per_group
  elif people_per_group <= 40:
        total_K2 += people_per_group
  elif people_per_group > 40:
    total_Everest += people_per_group

  total_people += people_per_group


print(f'{total_Mussala / total_people * 100:.2f}%')
print(f'{total_Montblanc / total_people * 100:.2f}%')
print(f'{total_Kilimangaro / total_people * 100:.2f}%')
print(f'{total_K2 / total_people * 100:.2f}%')
print(f'{total_Everest / total_people * 100:.2f}%')



