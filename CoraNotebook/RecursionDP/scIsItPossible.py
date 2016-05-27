'''
2 Possible Operations
(x,y) -> (x+y, y)
(x,y) -> (x, y+x)

Given a, b, c, d, return "Yes" if it is possible to start with (a,b) 
and end with the pair (c,d). Otherwise return "No".

Sample Input
1
4
5
9
Sample Output
Yes
Explanation
(1,4) -> (5,4) -> (5,9)
'''
def  isitpossible(a, b, c, d):
    if a == c and b == d:
        return "Yes"
    elif a > c or b > d:
        return "No"
    
    if isitpossible(a+b, b, c, d) == "Yes" or isitpossible(a, a+b, c, d) == "Yes":
    	return "Yes"
    else:
        return "No"

print (isitpossible(1,4,5,9))
