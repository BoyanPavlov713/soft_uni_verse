name = input()
length = int(input())
break_time = int(input())
import math
free_time = break_time - (break_time/8 + break_time/4)
if free_time >= length:
    print(f'You have enough time to watch {name} and left with {math.ceil(free_time - length)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(length - free_time)} more minutes.")