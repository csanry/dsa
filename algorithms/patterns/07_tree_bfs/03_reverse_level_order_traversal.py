"""
Problem Statement
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
ie. the lowest level comes first.
You should populate the values of all nodes in each level from left to right in separate sub-arrays.
"""

# implementation
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            # add the node to the current level
            current_level.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.appendleft(current_level)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Reverse level order traversal: {traverse(root)}")


if __name__ == "__main__":
    main()  # [[9, 10, 5], [7, 1], [12]]


"""
Time Complexity
The time complexity of the above algorithm is O(N), where 'N' is the total number of nodes in the tree.
This is because we traverse each node once.

Space Complexity
The space complexity of the above algorithm will be O(N) as we need to return
a list containing the level order traversal.
We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level
(this could only happen at the lowest level),
We will need O(N) space to store in the queue.
"""
