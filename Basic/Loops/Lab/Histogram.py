n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0


for i in range(1,n + 1):
    num = int(input())
    if num < 200:
        p1 += 1
    elif num < 400:
        p2 += 1
    elif num < 600:
        p3 += 1
    elif num < 800:
        p4 += 1
    else:
        p5 += 1
total_p = p1 + p2 + p3 + p4 +p5
print(f'{(p1/total_p)*100:.2f}%')
print(f'{(p2/total_p)*100:.2f}%')
print(f'{(p3/total_p)*100:.2f}%')
print(f'{(p4/total_p)*100:.2f}%')
print(f'{(p5/total_p)*100:.2f}%')
