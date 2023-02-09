days = int(input())
initial_doctors = 7
treated = 0
untreated = 0

for i in range(1, days + 1):
    patients_daily = int(input())
    if untreated > treated and i % 3 == 0:
        initial_doctors += 1
    if patients_daily <= initial_doctors:
        treated += patients_daily
    else:
        treated += initial_doctors
        untreated += patients_daily - initial_doctors

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')
