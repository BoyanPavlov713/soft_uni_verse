start = int(input())
end = int(input())
magic_number = int(input())
combination = 0
flag = False

for num1 in range(start, end + 1):
    if flag:
        break
    for num2 in range(start, end + 1):
        combination += 1

        if num1 + num2 == magic_number:
            print(f"Combination N:{combination} ({num1} + {num2} = {magic_number})")
            flag = True
            break
if not flag:
    print(f"{combination} combinations - neither equals {magic_number}")