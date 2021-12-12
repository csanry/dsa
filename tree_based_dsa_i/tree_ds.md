# Trees

## Why use Trees?  

- A tree is a nonlinear hierarchical data structure that consists of nodes connected by edges

- Other structures (arrays, stack, linked list) are linear data structures that store data sequentially

- Therefore, the time complexity of linear data structures increases with the increase in data size

- Different tree data structures allow quicker and easier access to the data given its non-linear data structure

## Characteristics 

- Node -> contains a key or value, and points to its child nodes

- The last nodes of each path are leaf nodes (don't have a link)

- Edge -> Link between any two nodes

- Root -> top most node of a tree 

- Height of a node -> number of edges from the node to the deepest leaf 

- Depth of a node -> number of edges from the root to the node

- Height of tree -> height of the root node / depth of the deepest node

- The degree of a node -> total number of branches of that node

- Forest -> A collection of disjoint trees 

## Applications 

- 
```python
def
```

#### Complexity Analysis 

- Selection sort performs 
    - 1st cycle (n - 1) comparisons
    - 2nd cycle (n - 2) comparisons ...
    - last 1 comparison
    
- Hence the number of comparisons is an arithmetic progression 
    - (n-1) + (n-2) + ... + 1 = n(n-1)/2
    
- Which is O(n^2) complexity

- Another way to think about it 
    - Selection sort requires two loops (one nested) - hence complexity is n * n = n^2
    
- Time
    - The worst case is O(n^2), when the array is in descending order
    - Best case is still O(n^2) - array is already sorted
    - Average case is O(n^2), when the array elements are jumbled up

- Space -> O(1) inplace sorting > variable to store step is used 
