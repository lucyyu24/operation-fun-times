## Depth First Search

starts at the root and explores as far as possible along each branch before backtracking


##### Pseudocode

![alt text](https://upload.wikimedia.org/wikipedia/commons/6/61/Graph.traversal.example.svg "Graph")

non-recursive solution:
will visit the nodes in order of A, E, F, B, D, C, G
```
procedure DFS-iterative(G,v):
    let S be a stack
    S.push(v)
    while S is not empty
          v = S.pop()
          if v is not labeled as discovered:
              label v as discovered
              for all edges from v to w in G.adjacentEdges(v) do
                  S.push(w)
```

recursive solution:
will visit the nodes in order of A, B, D, F, E, C, G
```
procedure DFS(G,v):
    label v as discovered
    for all edges from v to w in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G,w)
```

## Breadth First Search

starts at the root and explores the neighbour nodes first, before moving to the next level neighbours




