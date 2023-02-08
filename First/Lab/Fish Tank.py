length: int = int(input())
width = int(input())
height = int(input())
percentage = int(input())/100
volume = (length * width * height / 1000 ) *(1 - percentage)
print(volume)