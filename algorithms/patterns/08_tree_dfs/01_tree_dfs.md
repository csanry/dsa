# Tree Depth First Search

- This pattern is based on the Depth First Serarch (DFS) technique to traverse a tree.

- We will be using recursion to track parent nodes while traversing.

- A stack can be used for the iterative approach.

## Ways to identify

1. Problems dealing with tree like structures

2. Problems requiring to traverse trees depth first

## Problems

### [Binary Tree Path Sum](./02_binary_tree_path_sum.py)

> Given a binary tree and a number `S`, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals `S`.

- Since we are trying to search for a root-to-leaf path, we can use DFS to find a solution more efficiently

- To traverse the binary tree in a DFS fashion, we start from the root, making two recursive calls for the child nodes

    1. Start at the root

    2. If the current node is not a leaf node, do two things:

        - Subtract the value of the current node from the given number to get a new sum $S^* = S - \text{node.val}$

        - Make two recursive calls for both the children of the current node with the new numbers

    3. At each step, see if the current node being visited is a leaf node and if the value is equal to current value of `S`

    4. If both these conditions are met, we have found a root-to-leaf path

    5. Otherwise, return `false`

- The time complexity of the above algorithm is $O(n)$, where `n` is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

- The space complexity of the above algorithm will be $O(n)$ in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (ie. every node has one child).


### [All Paths for Sum](./03_all_paths_for_sum.py)

> Given a binary tree and a number `S`, find all paths from root-to-leaf such that the sum of all the node values of each path equals `S`.

- We can follow a similar DFS approach as **Binary Tree Path Sum** with a few minor differences

- Every time we find a root-to-leaf path, we will store it in a list

- We will traverse all paths and will not stop processing after finding the first path


- The time complexity of the above algorithm is $O(n^2)$, where `n` is the total number of nodes in the tree. This is due to the fact that we traverse each node once (which will take $O(n)$), and for every leaf node, we might have to store its path (by making a copy of the current path) which will take $O(n)$.

- If we ignore the space required for the `all_paths` list, the space complexity of the above algorithm will be $O(n)$ in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (ie. every node has one child).
