def func(start, end):
    result = ''
    for i in range(char_one + 1, char_two):
        result += f'{chr(i)} '

    return result

char_one = ord(input())
char_two = ord(input())

print(func(char_one,char_two))