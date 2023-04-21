n = int(input())

synonyms = {}

for _ in range(n):
    word = input()
    value = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(value)


for alpha, all_synonyms in synonyms.items():
    print(f'{alpha} - {", ".join(all_synonyms)}')
