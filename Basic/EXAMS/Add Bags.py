
baggage_price_over_20kg = float(input())
kg_baggage = float(input())
days = int(input())
number_baggage = int(input())

price = 0
if kg_baggage < 10:
    price = .2 * baggage_price_over_20kg
elif 10 <= kg_baggage <= 20:
    price = .5 * baggage_price_over_20kg
elif kg_baggage > 20:
    price = baggage_price_over_20kg

if days > 30:
    price *= 1.1
elif 7 <= days <= 30:
    price *= 1.15
else:
    price *= 1.4

total_price = price * number_baggage

print(f"The total price of bags is: {total_price:.2f} lv. ")
