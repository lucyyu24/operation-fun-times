# Heap

### Priority Queue Review

`Main Idea`: Stores items with keys that represent the priority the item has

###### Two Operations:

1. Insertion with a given key
2. Deletion of item with the max priority

### Heap

`Main Idea`: Implements priority queue efficiently by knowing very easily what the max element is, and thus we make all other elements follow from it.

How? The heap is a tree where each element keeps track of candidates that can replace them when they're deleted, as children. 

`Max Heap Property`: *Keys* of parent nodes are always greater than or equal to those of the children, thus the max element is the root. Vice versa for a min heap.

`Shape Property`: Is a *complete binary tree*. All levels except lowest level must be filled. If the last level of the tree is not complete, the nodes of that level are filled from left to right. Notice below, you cannot add children to 3 until 17 has two children.

![Max-Heap](https://upload.wikimedia.org/wikipedia/commons/3/38/Max-Heap.svg)

###### Summary of Heap Properties
- Highest priority element always stored at root (or lowest for min heap)
- Not a sorted structure (partially ordered)
- A complete bin tree has the smallest possible height
	- Shape property ensures that a heap with N nodes always has log N height
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

`Insertion` is a standard tree insertion that satisfies the shape property. It is O(log n) because the shape property ensures the height of tthe tree is O(log n).