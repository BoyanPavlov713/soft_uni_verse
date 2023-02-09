v =  int(input())
P1 = int(input())
P2 = int(input())
h = float(input())
full = ((P1 + P2) * h)
if full > v :
    print(f"For {h: .2f} hours the pool overflows with {full - v : .2f} liters.")
else:

    fullness = (full / v ) * 100
    P1_contribute = (P1 * h / full) * 100
    P2_contribute = (P2 * h / full) * 100
    print(f"The pool is {fullness : .2f}% full. Pipe 1: {P1_contribute: .2f}%. Pipe 2: {P2_contribute: .2f}%.")


