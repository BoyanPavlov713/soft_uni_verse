licence_plate_by_name = {}

count = int(input())
for _ in range(count):
    command_args = input().split()
    type_command = command_args[0]
    username = command_args[1]
    if len(command_args) >= 3:
        license_plate_number = command_args[2]
    if type_command == 'register':
        if username in licence_plate_by_name:
            print(f'ERROR: already registered with plate number {licence_plate_by_name[username]}')
        else:
            licence_plate_by_name[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif type_command == 'unregister':
        if username not in licence_plate_by_name:
            print(f"ERROR: user {username} not found")
        else:
            licence_plate_by_name.pop(username)
            print(f"{username} unregistered successfully")
for username, license_plate_number in licence_plate_by_name.items():
    print(f'{username} => {license_plate_number}')





