# * Undirected graph
# Remember if stmt on line 15
# https://www.hackerrank.com/challenges/bfsshortreach
# Doesn't pass test case #5 - runtime error; any idea?

def bfs(graph, start, nodes):
	visited, queue = [], [start]
	dist = [-1 for x in range(nodes)]
	dist[start-1] = 0 # [0,1,2,3]
	while queue:
		src = queue.pop(0)
		# print (src)
		visited.append(src)
		for dest in graph[src]:
			if dist[src-1] + 6 < dist[dest-1] or dist[dest-1] == -1:
				dist[dest-1] = dist[src-1] + 6
				queue.append(dest)
	dist.remove(0)
	print(*dist, sep=' ', end='\n')

numTests = int(input())
for i in range(numTests):
	numNodes, numEdges = map(int, input().split())
	graph = {}
	for j in range(numEdges):
		x, y = map(int, input().split())
		if x in graph:
			graph[x].append(y)
		else:
			graph[x] = [y]
		if y in graph:
			graph[y].append(x)
		else:
			graph[y] = [x]
	start = int(input())
	# print (graph)
	bfs(graph, start, numNodes)
