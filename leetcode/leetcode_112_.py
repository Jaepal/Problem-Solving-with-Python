"""
LeetCode 112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, root.val)]
        
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right:
                if val == sum:
                    return True
            if node.right:
                stack.append((node.right, val + node.right.val))
            if node.left:
                stack.append((node.left, val + node.left.val))