'''
Longest Common Substring
Find the longest common string that is a substring of two or more strings

O(mn) solution using DP
http://puu.sh/o5i67/f6e253ea9b.png

Note: If you want to find more than one substring, you can return a set of substrings
'''

def substr(s1,s2):
	arr = [[0 for x in range(len(s2))] for y in range(len(s1))]
	n = 0
	longest = ''
	for i in range(len(s1)):
		for j in range(len(s2)):
			if s1[i] == s2[j]:
				if i == 0 or j == 0:
					arr[i][j] = 1
				else:
					arr[i][j] = arr[i-1][j-1] + 1
				
				if arr[i][j] > n:
					n = arr[i][j]
					longest = s1[i-n+1:i+1]
				
	return longest


s1 = 'mycoolcatsarehere'
s2 = 'hercatsanddogs'

print(substr(s1,s2))