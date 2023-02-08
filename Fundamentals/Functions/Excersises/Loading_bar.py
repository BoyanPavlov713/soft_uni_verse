def loading_func(number):

    if number == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        load = f"[{(num//10) * '%'}{((10 - (num//10)) * '.')}]"
        print(f'{num}% {load}')
        print('Still loading...')
        return


num = int(input())
loading_func(num)



