# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res=-math.inf

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            temp=max(left,right,0)+node.val
            ans=max(temp,left+right+node.val)
            res=max(res,ans)
            return temp


        dfs(root)
        return res