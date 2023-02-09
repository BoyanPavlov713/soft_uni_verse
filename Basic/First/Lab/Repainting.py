nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
nylon_amount = (nylon + 2)*1.5
paint_amount = paint * 1.1 * 14.5
thinner_amount = thinner * 5
bags = 0.4
work = hours * (nylon_amount + paint_amount + thinner_amount + bags) * 0.3
print((nylon_amount + paint_amount + thinner_amount + bags) + work)
