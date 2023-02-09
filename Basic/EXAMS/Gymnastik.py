country = input()
tool = input()
difficulty = 0
execution = 0


if tool == 'ribbon':
    if country == 'Russia':
        difficulty = 9.1
        execution = 9.4
    elif country == 'Bulgaria':
        difficulty = 9.6
        execution = 9.4
    elif country == 'Italy':
        difficulty = 9.2
        execution = 9.5

if tool == 'hoop':
    if country == 'Russia':
        difficulty = 9.3
        execution = 9.8
    elif country == 'Bulgaria':
        difficulty = 9.55
        execution = 9.75
    elif country == 'Italy':
        difficulty = 9.45
        execution = 9.35

if tool == 'rope':
    if country == 'Russia':
        difficulty = 9.6
        execution = 9
    elif country == 'Bulgaria':
        difficulty = 9.5
        execution = 9.4
    elif country == 'Italy':
        difficulty = 9.7
        execution = 9.15

score = difficulty + execution
diff = abs(score - 20)
percent_diff = (diff / 20) * 100

print(f"The team of {country} get {score:.3f} on {tool}.")
print(f"{percent_diff:.2f}%")


