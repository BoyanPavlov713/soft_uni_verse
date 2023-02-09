w = int(input())
h = int(input())
total_pieces = 0
volume = w * h

pieces = input()

while pieces != 'STOP':
    pieces = int(pieces)
    total_pieces += pieces
    if total_pieces >= volume :
        break
    pieces = input()

diff = abs(volume - total_pieces)
if volume > total_pieces:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")