people = int(input())
capacity = int(input())
left = 0
coarses = 0

for i in range(people,0, -capacity):
    left -= capacity
    coarses += 1
print(coarses)