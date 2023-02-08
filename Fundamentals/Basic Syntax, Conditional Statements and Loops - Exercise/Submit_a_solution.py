divisor = int(input())
max = int(input())
for i in range(max,1,-1):
    if i % divisor == 0:
        print(i)
        break
