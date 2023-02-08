def calculates(comm , fst, secd):
    result = 0

    if operator == 'multiply':
        result = num1 * num2
    elif comm == 'divide':
        result = num1 // num2
    elif comm == 'add':
        result = num1 + num2
    elif comm == 'subtract':
        result = num1 - num2

    return result


operator = str(input())
num1 = int(input())
num2 = int(input())
res = calculates(operator, num1, num2)

print(res)
