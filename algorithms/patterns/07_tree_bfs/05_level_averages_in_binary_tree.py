"""
Problem Statement
Given a binary tree, populate an array to represent the averages of all of its levels.
"""

# implementation
from collections import deque


# instantiate a Tree class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        level_sum = 0
        for _ in range(level_size):
            current_node = queue.popleft()
            # add the node's value to the running sum
            level_sum += current_node.val
            # insert the children of current node in the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        # append the current level's average to the result array
        result.append(level_sum / level_size)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Level order traversal: {traverse(root)}")


if __name__ == "__main__":
    main()  # [12.0, 4.0, 6.5]


"""
Time Complexity
The time complexity of the above algorithm is O(N), where 'N' is the total number of nodes in the tree.
This is because we traverse each node once.

Space Complexity
The space complexity of the above algorithm will be O(N) which is required for the queue.
Since we can have a maximum of N/2 nodes at any level (this could only happen at the lowest level),
We will need O(N) space to store in the queue.
"""
