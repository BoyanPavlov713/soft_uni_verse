start = int(input())
end = int(input())
magic = int(input())
count = 0
flag = False

for x in range(start,end +1):
    for y in range(start,end +1):
        count += 1
        if x + y == magic:
            print(f"Combination N:{count} ({x} + {y} = {magic})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f'{count} combinations - neither equals {magic}')
