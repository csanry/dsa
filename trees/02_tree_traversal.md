# Tree Traversal

## Inorder, preorder and postorder

- Traversing a tree means visiting every node in a tree

- Unlike linear data structures like array, stacks, and queues, a hierarchical data structure like a tree can be traversed in different ways

## Intuition

- Binary trees are made up of nodes, which can contain up to two subtrees

```python
class Node:

    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item
```

- Given that our goal is to visit each node, traversing a binary tree involves the following subtasks

    - Visiting all the nodes in the left subtree

    - Visiting the root node

    - Visiting all the nodes in the right subtree

- The order of completion of tasks determines the kind of traversal

## Inorder traversal

- Follows the Left-Root-Right pattern

    - The left subtree is traversed first

    - Then the root node for that subtree is traversed

    - Finally, the right subtree is traversed

```python
def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)
        # Visit root
        print(str(root.val) + "->", end="")
        # Traverse right
        inorder(root.right)
```

## Preorder traversal

- Follows the Root-Left-Right pattern

```python
def preorder(root):
    if root:
        # Visit root
        print(str(root.val) + "->", end="")
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)
```

## Postorder traversal

- Follows the Left-Right-Root pattern

```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end="")
```

## Results

```python
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
```

```python
inorder(root) # 4->2->5->1->3->%
preorder(root) # 1->2->4->5->3->%
postorder(root) # 4->5->2->3->1->%
```
