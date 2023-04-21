key_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = {}
legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
crafted = False
while not crafted:
    line = input()
    materials = line.split()

    for idx in range(0, len(materials) - 1, 2):
        qnt = int(materials[idx])
        material = materials[idx + 1].lower()
        if material in key_items:
            key_items[material] += qnt
            if key_items[material] >= 250:
                key_items[material] -= 250
                crafted = True
                print(f'{legendary_items[material]} obtained!')
                break
        else:
            if material in junk_items:
                junk_items[material] += qnt
            else:
                junk_items[material] = qnt

for material, quantity in key_items.items():
    print(f'{material}: {quantity}')

for material, quantity in junk_items.items():
    print(f'{material}: {quantity}')
