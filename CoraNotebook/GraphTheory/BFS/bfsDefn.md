Pseudocode
```javascript
BFS (graph G, start):
	[all nodes initially unexplored]
	mark s as explored
	let Q = queue data struct (FIFO), initialized with S
	while !empty(Q):
		remove v the first node of Q, call it v
		for each edge (v,w):
			if w unexplored:
				mark w as explored
				add w to Q
```
Runtime
O(ns + ms) for main while loop
- where ns = # of nodes reachable from start s
- where ms = # of edges reachable from start s

Any given vertex v considered at most once
- Thus, ns

Any given edge (v,w) considered at most twice
1. Once when vertex v is being considered
2. Second time when vertex w is being considered
- Each edge visit is doing constant work O(1)

Therefore, linear time implementation
