text = input()
result = []
for char in text:
    if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
        result.append(char)

print(result)
