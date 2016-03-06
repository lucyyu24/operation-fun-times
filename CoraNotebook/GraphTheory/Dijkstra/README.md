# Dijkstra Shortest-Path Algorithm

A greedy algorithm to find the shortest paths between nodes in a graph. It allows for edges to have varying lengths.

![dijkstra graph](http://www.reviewmylife.co.uk/data/2008/0715/dijkstras-graph.gif)

####Important Assumption

Each edge has a non-negative length.*

####Pseudocode

```javascript
def Dijkstra(graph, src):
	Q = []							# vertex set Q
	for each vertex v in graph:
		dist[v] = infinity			# unknown dist from src
		prev[v] = undefined			# pointers to parent node for most optimal path
		add v to Q
	
	dist[src] = 0					# the only known dist, src to src
	
	while Q not empty:
		u = vertex in Q with min dist[u] 	# greedy property
		remove u from Q 

			for each neightbour v of u:
				temp = dist[u] + edgeLength(u,v)
				if temp < dist[v]:
					dist[v] = temp
					prev[v] = u
```

###### Note
- Dijkstra is a greedy algorithm for the shortest path, and that is demonstrated by `u = vertex in Q with min dist[u]`. It finds the node with the shortest edge from the current node. 

- Think of `prev` as an array that stores pointers to the next node in the shortest path. Thus, iterating through prev will give you the nodes for which to travel to obtain the shortest path.

- `if temp < dist[v]` is a critical difference between BFS and Dijkstra. A path to a certain node may have already been found, but this new path may have a shorter distance (temp) to that node due to the fact that all edges may vary in length.

###*Questions

####When could an edge be non-negative?

Computing a sequence of decisions, such as buying or selling stocks, may be thought of as a positive or negative value. Thus, not all edges in this series of decisions will have a positive value. In this case, *Dijkstra is not the appropriate algorithm to compute the most optimal path.* Other algorithms, such as Bellman-Ford involving DP would be more suitable.

####Why not just add a constant to all edges to avoid having negative-valued edges, and thus be able to use Dijkstra?

*It doesn't preserve the shortest path.*

![neg edges](http://puu.sh/nsGkJ/a857bda366.png)

In this case, original edges had values of 1, -5, and -2 in pink. The shortest path from s to t is surely by travelling from s -> v -> t, which has a score of -1 + (-5) = -4.

From our question before, to make all edges positive, we've added -5 to all edges to attempt to use Dijkstra to satisfy our important assumption. This produces edges with values of 6, 0, 3 in green. Now, the shortest path from s to t is to travel directly from s -> t, which has a score of 3.

This is due to the fact that there is only 1 edge on the bottom path, and thus only 5 was added to the bottom path. In contrast, there are two edges in the top path, and thus 10 was added to the top path.

Therefore, this counterexample shows you cannot simply add a constant value to each edge to product a graph with non-negative edges.

#####Another way to look at why Dijkstra cannot be applied to a graph with negative edges:

Dijkstra is a **greedy** algorithm based on the nodes that are one edge away from the current node. 

![neg greedy](http://puu.sh/nsHtI/d99773fea6.png)

It will first find that travelling from s -> t (score of -2) is less costly than travelling first from s -> v (score of 1). Thus it will now assume t has been visited and will be added to the list of conquered nodes, which assumes that the shortest path to this node has already been calculated.

####Runtime

Running Time
n = number of nodes in a graph
m = number of edges in a graph

From the while loop of the pseudocode, Dijkstra seemingly runs **O(mn)** time.
There are (n-1) iterations in the while loop. Within each iteration, we do a linear scan through all edges eligble, which is O(m) time with O(1) work per edge. 

###Can We do Better?

Yes. Use a **heap**. This finds minimums in logarithmic time rather than linear time in the above implementation.
