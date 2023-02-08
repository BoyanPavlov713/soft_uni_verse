import random

score = 0
for i in range(1,6):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct = num1 + num2
    print(num1, '+', num2, '=')
    answer = int(input('Your answer is : '))
    print()
    if answer == num1 + num2:
        score += 1
    if score == 5 :
        print(f'You scored {score} out of 5 ')
    elif score >= 3:
        print(f'Good, you score {score} out of 5')
    else:
        print(f'Need to learn math , you score {score} out of 5')

