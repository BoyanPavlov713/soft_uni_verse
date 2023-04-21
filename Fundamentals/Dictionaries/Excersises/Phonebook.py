phonebook = {}
n = 0

while True:
    line = input()
    parts = line.split('-')
    if len(parts) == 1:
        n = int(line)
        break

    name = parts[0]
    number = parts[1]

    phonebook[name] = number

for _ in range(n):
    searched_name = input()
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook.get(searched_name)}')
    else:
        print(f'Contact {searched_name} does not exist.')





