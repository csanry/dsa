"""
Problem Statement
Find the minimum depth of a binary tree.
The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""

# implementation
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    # exception case
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    minimum_tree_depth = 0
    while queue:
        minimum_tree_depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()

            # check if this is a leaf node
            if not current_node.left and not current_node.right:
                return minimum_tree_depth

            # insert the children of current node if not leaf node
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Tree Minimum Depth: {find_minimum_depth(root)}")  # 2
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print(f"Tree Minimum Depth: {find_minimum_depth(root)}")  # 3


main()

"""
Time Complexity
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
This is due to the fact that we traverse each node once.

Space Complexity
The space complexity of the above algorithm will be O(N) which is required for the queue.
Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level),
therefore we will need O(N) space to store them in the queue.
"""
