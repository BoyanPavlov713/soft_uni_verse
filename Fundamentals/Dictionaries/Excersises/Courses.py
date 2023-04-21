studsents_by_course = {}

while True:
    data = input()
    if data == 'end':
        break
    args = data.split(' : ')
    course_name = args[0]
    student_name = args[1]

    if course_name not in studsents_by_course:
        studsents_by_course[course_name] = []
    studsents_by_course[course_name].append(student_name)

for course_name, number in studsents_by_course.items():
    print(f'{course_name}: {len(number)}')

    for student in number:
        print(f'-- {student}')


