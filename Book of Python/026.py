word = input('Enter the word: ')
first = word[0]
rest = word[1:len(word)]
if first != 'a' and first != 'e' and first != 'i' and first != 'o' and first != 'u':
    newone = rest + first + 'way'
else:
    newone = word + 'way'
print(newone.lower())