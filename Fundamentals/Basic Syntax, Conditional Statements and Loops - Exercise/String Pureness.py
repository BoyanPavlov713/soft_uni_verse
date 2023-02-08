n = int(input())


for _ in range(n):
    word = input()
    flag = True

    for ch in word:
        if ch == '.' or ch == '_' or ch == ",":
            flag = False
            break
    if flag :
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")






