numbers =[int(x) for x in input().split()]
count = int(input())

for _ in range(count):
    numbers_to_remove = min(numbers)
    numbers.remove(numbers_to_remove)
print(', '.join([str(x) for x in numbers]))

