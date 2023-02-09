failed_score = int(input())

failed = 0
number_problems = 0
total_score = 0
flag = False
last_problem = ''

while failed < failed_score:
    name = input()
    if name == 'Enough':
        flag = True
        break
    score = int(input())

    if score <= 4:
        failed += 1
    total_score += score
    number_problems += 1
    last_problem = name

if flag:
    print(f'Average score: {total_score / number_problems:.2f}')
    print(f'Number of problems: {number_problems}')
    print(f'Last problem: {last_problem}')
else:
    print(f'You need a break, {failed} poor grades.')




