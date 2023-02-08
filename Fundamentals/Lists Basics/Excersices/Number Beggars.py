numbers = input().split(", ")
beggar_count = int(input())
beggars = [0] * beggar_count

for idx in range(len(numbers)):
    beggar_idx = idx % beggar_count
    num = int(numbers[idx])
    beggars[beggar_idx] += num

print(beggars)
