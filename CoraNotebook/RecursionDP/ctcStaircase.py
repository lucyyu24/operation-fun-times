'''
Staircase with n steps can be climbed by either 1 step, 2 steps, or 3 steps at a time.
How many ways are there to climb this set of stairs?
'''
def stepComb(rem, seen):
	if rem < 0:
		return 0
	if rem == 0:
		return 1
	if seen[rem] > 0:
		return seen[rem]
	else:
		seen[rem] = stepComb(rem-1, seen) + stepComb(rem-2, seen) + stepComb(rem-3, seen)
		return seen[rem]

n = 10
seen = [-1 for x in range(n+1)]
print (stepComb(n, seen))
