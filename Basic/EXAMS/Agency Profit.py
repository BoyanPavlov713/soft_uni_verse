name = input()
adults = int(input())
kids = int(input())
price = float(input())
tax_per_ticket = float(input())

price_tickets = adults * (price + tax_per_ticket) + kids * (price * .3 + tax_per_ticket)
profit = .2 * price_tickets
print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")