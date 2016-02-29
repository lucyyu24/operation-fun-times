graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'F'],
         'C': ['G', 'A'],
         'D': ['B'],
         'E': ['A', 'F'],
         'F': ['B', 'E'],
         'G': ['C']}

def BFS(graph, root):
	visited, queue = [root],[root]
	while queue:
		v = queue.pop()
		print(v)
		for i in graph[v]:
			if i not in visited:
				visited.append(i)
				queue.insert(0,i)

print ('BFS')
BFS(graph, 'A')
