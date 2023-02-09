name = input()
grade = 0
total_score = 0
failed = 0

while True:
    current_score = float(input())
    grade += 1

    if current_score < 4:
        failed += 1
        if failed > 1:
            print(f'{name} has been excluded at {grade} grade')
            break
        grade -= 1
    else:
        total_score += current_score
        if grade == 12:
            average_score = total_score / 12
            print(f'{name} graduated. Average grade: {average_score:.2f}')
            break





