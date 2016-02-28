### Depth First Search

starts at the root and explores as far as possible along each branch before backtracking

### Pseudocode

non-recursive solution
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

recursive solution
```
procedure DFS(G,v):
    label v as discovered
    for all edges from v to w in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G,w)
```
