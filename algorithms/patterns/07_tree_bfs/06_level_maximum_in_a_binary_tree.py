"""
Problem Statement
Find the largest value on each level of a binary tree.
"""

# implementation
from collections import deque
from math import inf


# instantiate a Tree class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def level_maximum(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        level_max = -inf
        for _ in range(level_size):
            current_node = queue.popleft()
            # recalculate the level's max
            level_max = max(level_max, current_node.val)
            # insert the children of current node in the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(level_max)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Level order traversal: {level_maximum(root)}")


if __name__ == "__main__":
    main()  # output [12, 7, 10]


"""
Time Complexity
The time complexity of the above algorithm is O(N), where 'N' is the total number of nodes in the tree.
This is because we traverse each node once.

Space Complexity
The space complexity of the above algorithm will be O(N) as we need to return a list
containing the level order traversal.
Since we can have a maximum of N/2 nodes at any level (this could only happen at the lowest level),
We will need O(N) space to store in the queue.
"""
