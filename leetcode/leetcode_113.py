"""
LeetCode 113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        
        stack = [(root, root.val, [root.val])]
        
        while stack:
            node, val, path = stack.pop()
            
            if not node.left and not node.right:
                if val == sum:
                    ans.append(path)
            if node.right:
                stack.append((node.right, val + node.right.val, path + [node.right.val]))
            if node.left:
                stack.append((node.left, val + node.left.val, path + [node.left.val]))
        
        return ans