days_off = int(input())
needed_play = 30000
work_days = 365 - days_off
play_time = days_off * 127 + work_days * 63
difference = abs(play_time - needed_play)
play_time_hour = (abs(play_time - needed_play) // 60)
play_time_min = abs(difference - play_time_hour * 60)

if play_time > needed_play :
    print("Tom will run away")
    print(f'{play_time_hour} hours and {play_time_min} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{play_time_hour} hours and {play_time_min} minutes less for play')


