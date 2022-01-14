'''
Similar Problems
Problem 1: Given a binary tree, find its maximum depth (or height).
Solution: We will follow a similar approach. Instead of returning as soon as we find a leaf node,
we will keep traversing for all the levels, incrementing maximumDepth each time we complete a level.
Here is what the code will look like:
'''

# implementation
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def find_maximum_depth(root):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    maximum_tree_depth = 0
    while queue:
        maximum_tree_depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()

            # insert the children of current node in queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return maximum_tree_depth

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Tree Maximum Depth: {find_maximum_depth(root)}") # 3
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print(f"Tree Maximum Depth: {find_maximum_depth(root)}") # 4

main()

'''
Time Complexity 
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once.

Space Complexity 
The space complexity of the above algorithm will be O(N) which is required for the queue. 
Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), 
therefore we will need O(N) space to store them in the queue.
'''