import random
toss = random.choice(['h','t'])
guess = input("Enter either (h)eads or (t)ail: ")
if guess == toss:
    print('You guessed right')
else:
    print("Bad Luck")
if toss == 'h':
    print('It was Heads')
else:
    print('It was tails')

