n = int(input())
total_price = 0

for _ in range(n):
    ppc = float(input())
    days = int(input())
    capsules = int(input())
    price = ppc * days * capsules
    if 0.01 <= ppc <= 100 and 1 <= days <= 31 and 1 <= capsules <= 2000:
        print(f"The price for the coffee is: ${price:.2f}")
    else:
        continue
    total_price += price

print(f"Total: ${total_price:.2f}")
