fuel = input()
liters = float(input())

if liters >= 25 :
    if fuel == "Gas" :
      print(f'You have enough gas.')
    elif fuel == "Gasoline" :
        print(f'You have enough gasoline.')
    elif fuel == "Diesel" :
        print(f'You have enough diesel.')
    else:
       print('Invalid fuel!.')

if liters < 25 :
    if fuel == "Gas":
        print(f'Fill your tank with gas!')
    elif fuel == "Gasoline":
        print(f'Fill your tank with gasoline!')
    elif fuel == "Diesel":
        print(f'Fill your tank with diesel!')
    else :
     print('Invalid fuel!')


