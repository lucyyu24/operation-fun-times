'''
Compute all permutations of a string of unique characters.
'''

def permute (s, chars):
	if not len(chars):
		print (s)

	for i in range(len(chars)):
		remChars = chars[:i] + chars[i+1:]
		permute (s+chars[i], remChars)

s = 'cats'
chars = list(s.strip())
permute ('', chars)
