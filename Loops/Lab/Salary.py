tabs = int(input())
salary = int(input())

for i in range(1,tabs +1):
    text = input()
    if text == 'Facebook':
        salary -= 150
    elif text == 'Instagram':
        salary -= 100
    elif text == 'Reddit':
        salary -= 50

    if salary <= 0:
        break
if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)
