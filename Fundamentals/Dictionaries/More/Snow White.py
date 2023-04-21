dwarfs = {}
hats = {}


while True:
    name, hat_colour, physics = input().split('<:>')
    if input() == 'Once upon a time':
        break

    key = name, hat_colour
    value = int(physics)

    if key in dwarfs:
        dwarfs[key] = max(value, dwarfs[key])
    else:
        dwarfs[key] = value
    if hat_colour in hats:
        hats[hat_colour] = 0
    hats[hat_colour] = name

    print(f'({hat_colour}) {name} <-> {physics}')





