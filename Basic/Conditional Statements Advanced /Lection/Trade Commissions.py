city = input()
sells = float(input())
discount = 0

if city == 'Sofia':
    if 0 <= sells  <= 500:
        discount = 0.05
    elif 500 < sells <=1000:
        discount = 0.07
    elif 1000 < sells <=10000:
        discount = 0.08
    elif sells > 10000:
        discount = 0.12
    else:
      print('error')
    if sells >= 0:
      print(f'{sells * discount:.2f}')

elif city == 'Varna':
    if 0 <= sells  <= 500:
        discount = 0.045
    elif 500 < sells <=1000:
        discount = 0.075
    elif 1000 < sells <=10000:
        discount = 0.1
    elif sells > 10000:
        discount = 0.13
    else:
      print('error')
    if sells >= 0:
        print(f'{sells * discount:.2f}')

elif city == 'Plovdiv':
    if 0 <= sells  <= 500:
        discount = 0.055
    elif 500 < sells <=1000:
        discount = 0.08
    elif 1000 < sells <=10000:
        discount = 0.12
    elif sells > 10000:
        discount = 0.145
    else:
      print('error')
    if sells >= 0:
     print(f'{sells * discount:.2f}')
else:
    print('error')










