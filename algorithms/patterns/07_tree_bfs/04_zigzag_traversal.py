"""
Problem Statement
Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right,
then right to left for the next level and keep alternating in the same manner for the following levels.

"""

# implementation
from collections import deque


# instantiate a Tree class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def zigzag_traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    left_to_right = True
    while queue:
        level_size = len(queue)
        current_level = deque()
        for _ in range(level_size):
            current_node = queue.popleft()
            # add the node to the current level based on the traversal direction
            if left_to_right:
                current_level.append(current_node.val)
            else:
                current_level.appendleft(current_node.val)

            # insert the children of current node in the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(list(current_level))
        # reverse the traversal direction
        left_to_right = not left_to_right

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print(f"Zigzag traversal: {zigzag_traverse(root)}")


if __name__ == "__main__":
    main()  # output [[12], [1, 7], [9, 10, 5], [17, 20]]


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
