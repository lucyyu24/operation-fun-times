'''
Write a program to sort a stack in ascending order. 
You should not make any assump- tions about how the stack is implemented. 
The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.

- Can just use one extra stack to sort the original stack
'''

stack = [6,4,9,1,2,3]
asc = []
temp = None

while stack or temp:
	if not temp:
		temp = stack.pop()
	if asc:
		if asc[-1] <= temp:
			asc.append(temp)
			temp = None
		else:
			stack.append(asc.pop())
	else:
		asc.append(temp)
		temp = None

print (asc)
