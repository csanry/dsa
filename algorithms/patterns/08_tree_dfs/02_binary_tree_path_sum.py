"""
Problem Statement
Given a binary tree and a number `S`,
find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals `S`.
"""


# instantiate a Tree class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def has_path(root, sum):
    if root is None:
        return False

    if root.val == sum and root.left is None and root.right is None:
        return True

    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Tree has path: {has_path(root, 23)}")  # True
    print(f"Tree has path: {has_path(root, 16)}")  # False


if __name__ == "__main__":
    main()


"""
Time Complexity
The time complexity of the above algorithm is O(N), where 'N' is the total number of nodes in the tree.
This is because we traverse each node once.

Space Complexity
The space complexity of the above algorithm will be O(N). This space is used to store the recursion stack
in the worst case.
The worst case happens when the given tree is a linked list.
"""
