# Trees

## Why use Trees?

- A tree is a `nonlinear hierarchical` data structure that consists of nodes connected by edges

- Other structures (arrays, stack, linked list) are `linear data structures` that store data sequentially

- Therefore, the time complexity of linear data structures increases with the increase in data size

- Different tree data structures allow quicker and easier access to the data given its non-linear data structure

## Characteristics

- Node $\rarr$ contains a key or value, and points to its child nodes

    - The last nodes of each path are leaf nodes (don't have a link)

- Edge $\rarr$ Link between any two nodes

- Root $\rarr$ top most node of a tree

- Height of a node $\rarr$ number of edges from the node to the deepest leaf

- Depth of a node $\rarr$ number of edges from the root to the node

- Height of tree $\rarr$ height of the root node / depth of the deepest node

- The degree of a node $\rarr$ total number of branches of that node

- Forest $\rarr$ A collection of disjoint trees

## Traversal

- A common subtask when performing operations on a tree is to reach nodes in the tree

- Various [tree traversal algorithms]() help to visit various nodes in a tree

## Tree Applications

- A binary search tree (BST) is used to quickly check whether an element is present in a set

- A heap is a kind of tree that can be used for heap sort

- Most popular databases use B-Trees and T-Trees, which are variants of the tree structure that are used to store data
