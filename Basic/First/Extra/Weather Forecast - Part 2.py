forecast = float(input())
if 26.00 <=forecast <= 35.00 :
    print("Hot")
if  20.10<= forecast <= 25.99:
    print("Warm")
if  15.00 <= forecast <= 20.09:
    print("Mild")
if 12.00 <= forecast <= 14.99:
    print("Cool")
if  5.00<= forecast <=11.99:
    print("Cold")
if 35.00 <= forecast or forecast < 5.00:
    print("unknown")





