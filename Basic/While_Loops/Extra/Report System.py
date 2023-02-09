needed_sum = int(input())
count = 1
total = 0
cash = 0
card = 0
cash_count = 0
card_count = 0
current_sum = input()

while total < needed_sum:
    if current_sum == 'End':
        break
    if current_sum != 'End':
        current_sum = int(current_sum)

    if count % 2 != 0:
        if current_sum > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cash += current_sum
            cash_count += 1
    elif count % 2 == 0:
        if current_sum < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            card += current_sum
            card_count += 1

    count += 1
    total = cash + card
    current_sum = input()

if total > needed_sum:
        print(f'Average CS: {cash / cash_count:.2f}')
        print(f"Average CC: {card / card_count:.2f}")

else:
    print("Failed to collect required money for charity.")








