capacity = int(input())
all_fans = int(input())
a_count = 0
b_count = 0
v_count = 0
g_count = 0

for i in range(1,all_fans +1):
    sector = input()
    if sector == 'A':
        a_count += 1
    elif sector == 'B':
        b_count += 1
    elif sector == 'V':
        v_count += 1
    elif sector == 'G':
        g_count += 1
print(f'{a_count / all_fans * 100:.2f}%')
print(f'{b_count / all_fans * 100:.2f}%')
print(f'{v_count / all_fans * 100:.2f}%')
print(f'{g_count / all_fans * 100:.2f}%')
print(f'{all_fans / capacity * 100:.2f}%')