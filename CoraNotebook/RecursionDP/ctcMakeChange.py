'''
Given an infinite number of quarters, dimes, nickels, and pennies, find the number of ways to represetn n cents.
'''

def cashMoney (n, coinIndex, coins):
	coin = coins[coinIndex]
	combs = 0
	coinCount = 0

	if coin == 1: # only one combo with all pennies
		return 1

	while coinCount*coin <= n:
		combs += cashMoney (n-coinCount*coin, coinIndex+1, coins)
		coinCount += 1

	return combs

n = 200
coins = [25, 10, 5, 1]
print(cashMoney(n, 0, coins))
