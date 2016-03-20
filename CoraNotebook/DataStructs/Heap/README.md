# Heap

### Priority Queue Review

`Main Idea`: Stores items with keys that represent the priority the item has

###### Two Operations:

1. Insertion with a given key
2. Deletion of item with the max priority

### Heap

`Main Idea`: Implements priority queue efficiently by knowing very easily what the max element is, and thus we make all other elements follow from it.

How? The heap is a tree where each element keeps track of candidates that can replace them when they're deleted, as children. 

`Heap-Order Property`: *Keys* (priorities) of parent nodes are always greater than or equal to those of the children, thus the max element is the root. Vice versa for a min heap.

`Structural Property`: Is a *complete binary tree*. All levels except lowest level must be filled. If the last level of the tree is not complete, the nodes of that level are filled from left to right (left-justified). Notice below, you cannot add children to 3 until 17 has two children.

![Max-Heap](https://upload.wikimedia.org/wikipedia/commons/3/38/Max-Heap.svg)

###### Summary of Heap Properties
- Highest priority element always stored at root (or lowest for min heap)
- Not a sorted structure (partially ordered)
- A complete bin tree has the smallest possible height
	- Structural property ensures that a heap with N nodes always has log N height
- Useful when you need to remove the object with the highest (or lowest) priority, thus helps us with priority queues (yay!)

###### Uses
- [Dijkstra's](https://github.com/lucyyu24/operation-fun-times/tree/master/CoraNotebook/GraphTheory/Dijkstra) greedy algorithm

###### Running Time

|  			| Average 		| Worst Case 	|  
| ------	| --------------| -------------	|  
| Space 	|        O(n) 	|          O(n) |  
| Search	|        O(n) 	|          O(n) |  
| Insert 	|            	|          O(log n) |
| Delete 	|        O(log n) 	|          O(log n) |  
| Peek	|        O(1) 	|          O(1) |  


#### Insertion in Heaps
This is a standard tree insertion that satisfies the structural property. It is O(log n) because the shape property ensures the height of tthe tree is O(log n).

1. Place the new key at the first free leaf.
2. Since the heap-order property may be violated, do a *bubble-up*.

```javascript
bubbleUp(v):
v: a node of the heap
	while v.parent exists and v.parent.key < v.key:
		swap v and v.parent
		v = v.parent
```

The new item bubbles up until it reaches the correct place in the heap.

Time: O(height of heap) = O(log n)

Example Video: [bubble-up](https://www.youtube.com/watch?v=c1TpLRyQJ4w)

#### deleteMax in Heaps

Note a heap is not a binary search tree due to the structural-property to keep the tree left-justified at all times. Thus we cannot use the same delete algorithm.

1. The maximum item of a heap is the root node.
2. Replace the root by the last leaf to maintain the structure.
3. Since the heap-order property may be violated, do a *bubble-down*.

```javascript
bubbleDown(v):
v: a node of the heap
	while v is not a leaf:
		u = max(keys of v.children)
		if u.key > v.key:
			swap u and v
			v = u
		else:
			break
```

Time: O(height of heap) = O(log n)

Example Video: [bubble-down](https://www.youtube.com/watch?v=ijfPvX2qYOQ)

#### Storing Heaps in Arrays

If H were a heap with n items and A were an array of size n, store the root in A[0] and insert elements into the aray level-by-level from top to bottom, left-to-right.

`Left Child` of A\[i\] (if it exists) is A[2i + 1]

`Right Child` of A\[i\] (if it exists) is A[2i + 2]

`Parent` of A\[i\] (i != 0) is A[(i-1)/2]

![Heap as an Array](http://www.algolist.net/img/binary-heap-array-mapping.png)

#### Building Heap

Given n items (in A[0...n-1]) build a heap. The array is unsorted.

```javascript
heapify(A)
A: an array
	n = size(A) - 1
	for i in range(n/2, 0, -1):
		bubbleDown(A,i)
```

Worse-Case Complexity: O(n)

A heap can be built in linear time!

###### Why isn't it O(n log n)?

Inserting an item into the heap is O(log n), which is repeated n/2 times (the rest are leaves, and can't violate heap property and thus you don't need to bubble down). Wouldn't that be O(n log n) then?

![Bubble Downs](https://upload.wikimedia.org/wikipedia/commons/a/ac/Binary_heap_bottomup_vs_topdown.svg)

This diagram shows that in the bottommost level, there are 2^(h) nodes, but they can't bubble down anymore, so the work is 0. The next level there are 2^(h-1) nodes, and each may bubble down by 1 level. At the third level, there are 2^(h-2) nodes, and each may bubble down by 2 levels. Therefore, **not all bubble down operations are O(log n)**, and thus building a heap from an array is O(n).

