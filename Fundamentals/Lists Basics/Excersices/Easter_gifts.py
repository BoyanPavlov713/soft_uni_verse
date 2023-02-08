gifts = input().split()

while True:
    line = input()
    if line == "No Money":
        break

    command_args = line.split()
    command = command_args[0]
    gift = command_args[1]

    if command == 'OutOfStock':
        pass

    elif command == 'Required':
        idx = int(command_args[2])
    elif command == "JustInCase":
        pass






