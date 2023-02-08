n = int(input())
word = input()
my_list = []
word_list = []

for i in range(n):
    speech = input()
    my_list.append(speech)
    if word in speech:
        word_list.append(speech)

print(my_list)
print(word_list)
