exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
# •	"Early", ако студентът пристига повече от 30 минути преди часа на изпита.
min_exam = exam_hour * 60 +exam_minutes
min_arrival = arrival_hour * 60 + arrival_minutes
diff = abs(min_arrival - min_exam)

if min_arrival > min_exam :
    print("Late")
    if diff >= 60:
     print(f'{diff // 60}:{diff % 60:02d} hours after the start')
    else:
        print(f'{diff} minutes after the start')

elif 30 >= min_exam - min_arrival >= 0:
    print('On time')
    print(f'{diff} minutes before the start')

elif 30 < min_exam - min_arrival:
    print("Early")
    if diff >= 60:
     print(f'{diff // 60}:{diff % 60:02d} hours before the start')
    else:
        print(f'{diff} minutes before the start')


