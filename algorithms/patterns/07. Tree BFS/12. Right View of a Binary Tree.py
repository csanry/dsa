'''
Problem Challenge 2
Given a binary tree, return an array containing nodes in its right view.
The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
'''

from __future__ import print_function
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def tree_right_view(root):

    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        for i in range(0, level_size):
            current_node = queue.popleft()
            # if it is the last node of this level, add it to the result
            if i == level_size - 1:
                result.append(current_node)
            # insert the children of the current node
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(3)
    result = tree_right_view(root)
    print('Tree right view: ')
    for node in result:
        print(f'{node.val} ', end='')

main()

'''
Time Complexity
The time complexity of the above algorithm is O(N), where 'N' is the total number of nodes in the tree.
This is because we traverse each node once.

Space Complexity
The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal.
We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could only happen at the lowest level),
We will need O(N) space to store in the queue. 
'''

'''
Similar Questions 
Problem 1: Given a binary tree, return an array containing nodes in its left view.
The left view of a binary tree is the set of nodes visible when the tree is seen from the left side.

Solution: 
A similar approach to tree right view can be followed, but instead of appending the last element of each level, we will append the first element of each level to the output array.
'''