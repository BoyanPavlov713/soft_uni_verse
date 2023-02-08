number_students = int(input())
top_students = 0
very_good_students = 0
good_students = 0
fail_students = 0
sum_score = 0

for i in range(1, number_students + 1):
    student_score = float(input())
    if student_score < 3:
        fail_students += 1
    elif student_score < 4:
        good_students += 1
    elif student_score < 5:
        very_good_students += 1
    else:
        top_students += 1
    sum_score += student_score

print(f'Top students: {top_students / number_students *100:.2f}%')
print(f'Between 4.00 and 4.99: {very_good_students / number_students *100:.2f}%')
print(f'Between 3.00 and 3.99: {good_students / number_students *100:.2f}%')
print(f'Fail: {fail_students / number_students *100:.2f}%')
print(f'Average: {sum_score / number_students:.2f}')



