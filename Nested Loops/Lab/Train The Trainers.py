jury = int(input())
presentation = input()
total_sum = 0
count_all_grades = 0

while presentation != 'Finish':

    sum_presentation_grades = 0

    for n in range(1, jury +1):
        grade = float(input())
        sum_presentation_grades += grade
        total_sum += grade
        count_all_grades += 1
    print(f"{presentation} - {sum_presentation_grades / jury:.2f}.")
    presentation = input()

print(f"Student's final assessment is {total_sum / count_all_grades:.2f}.")
