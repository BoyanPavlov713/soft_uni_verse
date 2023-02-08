hour = int(input())
min = int(input())

new_time = hour * 60 + min + 15

new_hour = new_time // 60
new_min = new_time % 60

if new_hour > 23:
    new_hour = 0

if new_min < 10:
    print(f'{new_hour}:0{new_min}')

else:
    print(f'{new_hour}:{new_min}')

