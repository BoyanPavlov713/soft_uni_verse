record_in_sec = float(input())
distance_in_meters = float(input())
time_per_m = float(input())

delay = (distance_in_meters // 50) * 30
speed = distance_in_meters * time_per_m
time = speed + delay
if time < record_in_sec :
    print(f'Yes! The new record is {time:.2f} seconds.')
else:
    print(f'No! He was {time - record_in_sec:.2f} seconds slower.')