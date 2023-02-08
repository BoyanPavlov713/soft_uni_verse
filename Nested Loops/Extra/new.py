
number = int(input())
count = 0
for n in range(1, number + 1):
    if number % n == 0:
        count += 1
if count == 2:
    print (number)
else:
    print('DAMN')