graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'F'],
         'C': ['G', 'A'],
         'D': ['B'],
         'E': ['A', 'F'],
         'F': ['B', 'E'],
         'G': ['C']}


'''
interative solution
'''

def DFS_iterative (graph, root):
	visited, stack = [], [root]
	while stack:
		v = stack.pop()
		if v not in visited:
			print(v)
			visited.append(v)
			for i in graph[v]:
				stack.append(i)

print ('DFS_iterative:')				
DFS_iterative(graph, 'A')


'''
recursive solution
'''

visited = []

def DFS_recursive (graph, v):
	print (v)
	visited.append(v)
	for i in graph[v]:
		if i not in visited:
			DFS_recursive(graph, i)

print ('DFS_recursive:')	
DFS_recursive(graph, 'A')