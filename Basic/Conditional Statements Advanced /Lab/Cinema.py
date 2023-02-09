type = input()
rows = int(input())
collums = int(input())
seats = rows * collums
if type == "Premiere":
    print(f'{12 * seats:.2f}')
elif type == "Normal":
    print(f'{7.5 * seats:.2f}')
elif type == "Discount":
    print(f'{5 * seats:.2f}')
