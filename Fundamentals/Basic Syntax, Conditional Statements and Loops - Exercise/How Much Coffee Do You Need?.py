coffee = 0

while True:
    event = input()
    if event == 'END':
        break
    if event == 'dog' or event == 'cat' or event == 'movie' or event == 'coding':
        coffee += 1
    elif event == 'CAT' or event == 'DOG' or event == 'MOVIE' or event == 'CODING':
        coffee += 2
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)