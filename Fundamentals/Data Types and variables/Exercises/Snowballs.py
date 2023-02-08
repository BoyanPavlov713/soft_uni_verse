n = int(input())
best = float('-inf')

for i in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value =(weight // time) ** quality

    if value > best:
        best = value
        ura = f"{weight} : {time} = {best} ({quality})"
print(ura)
