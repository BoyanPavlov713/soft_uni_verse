maxnumber = - 1000000000
best = ''
name = input()
while name != 'END':
    goals = int(input())

    if goals > maxnumber:
        maxnumber = goals
        best = name
    if goals >= 10:
        break
    if name == 'END':
            break
    name = input()

print(f"{best} is the best player!")
if goals >= 3:
    print(f"He has scored {maxnumber} goals and made a hat-trick !!!")
else:
    print(f"He has scored {maxnumber} goals.")






