max_num = - 1000000000

while True:
    num = input()
    if num == "Stop":
        break
    num = int(num)
    if num > max_num:
        max_num = num
print(max_num)