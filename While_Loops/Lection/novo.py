available_sum = 0
while True:
        curreent_sum = input()

        if curreent_sum == 'NoMoreMoney':
            break

        curreent_sum = float(curreent_sum)

        if curreent_sum >= 0:
            available_sum = available_sum + curreent_sum
            print(f'Increase: {curreent_sum:.2f}')
        else:
            print('Invalid operation!')
            break

print(f'Total: {available_sum:.2f}')