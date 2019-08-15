'''
LeetCode 104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
'''


def maxDepth(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1