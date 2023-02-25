#!/usr/bin/python3
""" Determines the fewest number of coins needed to meet a given amount total """


def makeChange(coins, total):
	ch = [total + 1] * (total + 1)
	ch[0] = 0

	for i in range(1, total + 1):
		for coin in coins:
			if i - coin >= 0:
				ch[i] = min(ch[i], 1 + ch[i - coin])

	if ch[total] != (total + 1):
		return ch[total]
	return -1
