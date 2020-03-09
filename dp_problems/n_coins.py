"""Finds the smallest number of coins for the sum S"""

INFINITY = 100000
COINS = [1, 3, 5, 10]
S = 201

min_coins = [INFINITY]*S
min_coins[0] = 0
i = 1
while i < S:
    j = 0
    while j < len(COINS):
        if COINS[j] <= i and min_coins[i - COINS[j]] + 1 < min_coins[i]:
            min_coins[i] = min_coins[i - COINS[j]] + 1
        j += 1
    i += 1

print(min_coins)
