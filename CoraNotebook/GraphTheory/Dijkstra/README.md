# Dijkstra Shortest-Path Algorithm

###Important Assumption

Each edge has a non-negative length.

##Questions

###When could an edge be non-negative?

Computing a sequence of decisions, such as buying or selling stocks, may be thought of as a positive or negative value. Thus, not all edges in this series of decisions will have a positive value. In this case, *Dijkstra is not the appropriate algorithm to compute the most optimal path.* Other algorithms, such as Bellman-Ford involving DP would be more suitable.

###Why not just add a constant to all edges to avoid having negative-valued edges, and thus be able to use Dijkstra?

*It doesn't preserve the shortest path.*

![neg edges](http://puu.sh/nsGkJ/a857bda366.png)

In this case, original edges had values of 1, -5, and -2 in pink. The shortest path from s to t is surely by travelling from s to v to t, which has a score of -1 + (-5) = -4.

From our question before, to make all edges positive, we've added -5 to all edges to attemp to use Dijkstra to satisfy our important assumption stated at the top of this doc. This produces edges with values of 6, 0, 3 in green. Now, the shortest path from s to t is to travel directly from s to t, which has a score of 3.

This is due to the fact that there is only 1 edge on the bottom path, and thus only 5 was added to the bottom path. In contrast, there are two edges in the top path, and thus 10 was added to the top path.

Therefore, this counterexample shows you cannot simply add a constant value to each edge to product a graph with non-negative edges.

#####Another way to look at why Dijkstra cannot be applied to a graph with negative edges:

Dijkstra is a **greedy** algorithm based on the nodes that are one edge away from the current node.

![neg greedy](http://puu.sh/nsHtI/d99773fea6.png)

It will first find that travelling from s -> t (score of -2) is less costly than travelling first from s -> v (score of 1). Thus it will now assume t has been visited and will be added to the list of conquered nodes, which assumes that the shortest path to this node has already been calculated.

Pseudocode

```javascript
X = [start] 	# visited nodes
A[start] = 0 	# only stores shortest distances

while X != V:
	among all edges (v,w) with v in X and w not in X, pick one that minimizes A[v] + l(v,w):
		add w* to X
		set A[w*] = A[v*] + l(v*,w*)
```

Note (v*, w*) denotes the minimum edge
Note Dijkstra's greedy criterion for picking the minimum A[v] + l(v,w)

Running Time
n = number of nodes in a graph
m = number of edges in a graph

From the while loop of the pseudocode, Dijkstra seemingly runs O(mn) time.
There are (n-1) iterations in the while loop. Within each iteration, we do a linear scan through all edges eligble, which is O(m) time with O(1) work per edge. 

###Can We do Better?

Yes. Use a **heap**. This finds minimums in logarithmic time rather than linear time in the above implementation.
