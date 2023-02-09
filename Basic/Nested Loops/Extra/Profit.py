one_lev_coins = int(input())
two_lev_coins = int(input())
five_lev_coins = int(input())
total = int(input())

for one_lev_coins in range(0, one_lev_coins +1):
    i = one_lev_coins * 1
    for two_lev_coins in range(0, two_lev_coins +1):
        j = two_lev_coins * 2
        for five_lev_coins in range(0, five_lev_coins +1):
            k = five_lev_coins * 5

            if total == i + j + k:
                print(f"{one_lev_coins} * 1 lv. + {two_lev_coins} * 2 lv. + {five_lev_coins} * 5 lv. = {total} lv.")