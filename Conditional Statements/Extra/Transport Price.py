km = int(input())
time = input()


if km < 20:

     if time == 'day':
        print(f"{0.7 + km * .79:.2f}")
     elif time =='night':
         print(f"{0.7 + 0.9 * km:.2f}")
if 20 <= km < 100:
         print(f"{km * 0.09:.2f}")

if km >= 100 :
        print(f"{km * 0.06:.2f}")


