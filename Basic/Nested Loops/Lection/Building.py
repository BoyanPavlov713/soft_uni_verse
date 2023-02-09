number_floors = int(input())
number_rooms = int(input())

for f in range(number_floors, 0, -1):
    for a in range(number_rooms):
        flat_number = 10 * f + a
        if f == number_floors:
            flat_type = f'L{flat_number}'
        elif f % 2 == 0:
            flat_type = f'O{flat_number}'
        elif f % 2 != 0:
            flat_type = f'A{flat_number}'

        print(flat_type, end=' ')
    print()

