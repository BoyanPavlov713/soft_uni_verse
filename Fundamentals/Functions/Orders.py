def account(item , qnt):
    """
    jhgjhgjhg
    :param item: jhjhg
    :param qnt: hgjhg
    :return: kjgkjg
    """
    return total_price


item = input()
num = int(input())
total_price = 0

if item == "coffee":
    total_price = 1.5 * num
elif item == "coke":
    total_price = 1.4 * num
elif item == "water":
    total_price = 1 * num
elif item == "snacks":
    total_price = 2 * num

account(item, num)
print(f'{total_price: .2f}')




