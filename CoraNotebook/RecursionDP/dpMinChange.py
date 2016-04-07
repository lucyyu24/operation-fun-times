'''
Use the least number of coins to make n change.
You may use 1, 5, 10, 25 valued coins.

Solution uses DP.
'''

def dpMakeChange(n, change):
	minChange = [0 for x in range(n+1)]

	for i in range (1, n+1):
		minChange[i] = n
		for c in change:
			if c <= i:
				if minChange[i-c] + 1 < minChange[i]: 
					minChange[i] = minChange[i-c] + 1

	return minChange[n]

change = [1,5,10,25]
n = 26
print(dpMakeChange(n, change))