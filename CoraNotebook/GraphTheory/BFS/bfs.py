def bfs(graph, start):
	visited, queue = [start], [start]
	while queue:
		v = queue.pop(0)
		print(v)
		for i in graph[v]:
			if i not in visited:
				queue.append(i)
				visited.append(i)

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

bfs(graph, 'A')

'''
General implementation of BFS
- traverses all nodes in a 'directed' graph
- it's 'directed' because of the way the graph is created
- ie. vertex A is accompanied by the list [B,C], meaning you can travel
from A to B and C
'''