
party = float(input())
love_messages = int(input())
roses = int(input())
key_chains = int(input())
pictures = int(input())
fortune_cookies = int(input())

gain = love_messages * .6 + roses * 7.2 + key_chains * 3.6 + pictures * 18.2 + fortune_cookies * 22
if love_messages + roses + key_chains + pictures + fortune_cookies > 25:
    gain = .65 * gain


ultimate_gain = .9 * gain

if ultimate_gain >= party:
    print(f"Yes! {ultimate_gain - party:.2f} lv left.")
else:
    print(f"Not enough money! {party - ultimate_gain:.2f} lv needed.")

