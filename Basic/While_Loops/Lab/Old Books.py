book = input()

count = 0
input_line = input()
flag = False

while input_line != 'No More Books':
    if input_line == book:
        flag = True
        break
    count += 1
    input_line = input()

if flag:
    print(f'You checked {count} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {count} books.')




