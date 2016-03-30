'''
Create valid combinations of brackets from n pairs of brackets
'''
def expand (leftRem, rightRem, s):
	if leftRem == 0 and rightRem == 0:
		print (s)
		return

	if leftRem < 0 or rightRem < leftRem: # brackets syntax error
		return
	else:
		expand (leftRem-1, rightRem, s + '(')
		expand (leftRem, rightRem-1, s + ')')

n = 3
expand (n, n, '')
