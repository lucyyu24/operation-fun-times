'''
Magic Index: Given a sorted array of distinct integers, write a method to find a magic index a[i] = i.
'''

def findIndex(n, start, end):
	if start == end:
		midIndex = start
	else:
		midIndex = (start+end)//2

	if midIndex == n[midIndex]:
		return midIndex
	elif start == end:
		return None
	elif midIndex > n[midIndex]:
		return findIndex(n, midIndex+1, end)
	else:
		return findIndex(n, start, midIndex-1)

x = [-1, 0, 1, 3]
x2 = [-1, 1, 3, 4, 5]
x3 = [6, 7, 8]
print(findIndex(x, 0, 3))