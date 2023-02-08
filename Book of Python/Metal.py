
favourite_band = "Bolt Thrower"
guess_limit = 3
tries = 0
while guess_limit > tries:
     guess = input('What is my death favourite band: ')
     tries += 1

     if guess == favourite_band:
         print("That is my favourite death metal band")
         break
     else:
         print('Not too bad but...try again!')
else:
    print('Shame on you!')



