magnolias = int(input())
zumbul = int(input())
roses = int(input())
cactus = int(input())
gift_price  = float(input())
import math
profit = .95*(magnolias * 3.25 + zumbul * 4 + roses* 3.5+ cactus * 8)
if profit >= gift_price :
    print(f"She is left with {math.floor(profit - gift_price)} leva." )
elif profit < gift_price :
    print(f"She will have to borrow {math.ceil(gift_price - profit)} leva." )