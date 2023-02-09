movie = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0
while movie != 'Finish':
    free_seats = int(input())
    type = input()
    current_tickets = 0

    while True:
        if type == 'student':
                student_tickets += 1
        elif type == 'standard':
             standard_tickets += 1
        elif type == 'kid':
                kid_tickets += 1

        if type == 'Finish'or current_tickets == free_seats:
            print(f"{movie} - {((current_tickets / free_seats) * 100):.2f}% full.")
            movie = type
            break
        elif type == 'End':
            print(f"{movie} - {((current_tickets / free_seats) * 100):.2f}% full.")
            movie = input()
            break

        current_tickets += 1
        total_tickets += 1
        type = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets *100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets *100:.2f}% standard tickets.")
print(f"{kid_tickets / total_tickets *100:.2f}% kids tickets.")








