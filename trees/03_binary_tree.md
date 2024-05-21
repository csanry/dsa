# Binary Tree

- A tree data structure where each parent node can have at most two children

- Typically nodes within the tree are represented with a data part and two pointer to other nodes

```python
class Node:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
```

## Types of binary trees

### Full binary tree

- Binary trees with an additional condition that every parent node has either two or no children

```
             _____14__
            /         \
       ____13__        9
      /        \      / \
     12         7    3   8
    /  \
   0    10
```

### Perfect binary tree

- A binary tree in which every internal node has exactly two child nodes, and all the leaf nodes are on the same level

```
            ______7_______
           /              \
        __3__           ___11___
       /     \         /        \
      1       5       9         _13
     / \     / \     / \       /   \
    0   2   4   6   8   10    12    14
```

### Complete binary tree

- Every level must be completely filled

- All leaves must lean towards the left

- The last leaf might not have a right sibling ie. a complete binary tree doesn't have to be a full binary tree

```
             _____14__
            /         \
       ____13__        9
      /        \      /
     12         7    3
```

### Degenerate tree

- A degenerate tree is a tree having only single childs (left or right)

```
            __7
           /
        __3
       /
      1
       \
        2
```

### Skewed binary tree

- A degenerate tree in which the tree is either dominated by the left nodes or right nodes

```
Left skewed binary tree

            _7
           /
        _3
       /
      1
     /
    0
```

## Balanced binary tree

- A binary tree in which the difference between the height of the left and the right subtree for each node is either 0 or 1

```
             _____14__ df=1
            /         \
       ____13__ df=0   9 df=0
      /        \
     12 df=0    7 df=0
```

## Applications

- For easy and quick access to data

- To implement a heap data structure
