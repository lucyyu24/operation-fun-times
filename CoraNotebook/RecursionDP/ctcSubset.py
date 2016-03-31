'''
Return all subsets of a set.
(Used an array instead of a set - TODO just use sets)
'''
def binToSet(b, s):
	subset = []
	bStr = str(b)
	for i in range(len(s)): 
		if bStr[i] == '1':
			subset.append(s[i])
	return subset

def findSubsets(inp):
	inSize = '{0:0' + str(len(inp)) + 'b}' # trust; it works
	allSubsets = []
	for i in range(2**len(inp)):
		binRep = inSize.format(i)
		allSubsets.append(binToSet(binRep, inp))
	return allSubsets


inp = [1,2,3]
for x in findSubsets(inp): print (x)
