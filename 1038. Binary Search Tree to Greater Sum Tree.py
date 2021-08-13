# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0

        def dfs(node):
            nonlocal total
            if not node:
                return None
            dfs(node.right)
            total += node.val
            node.val = total
            dfs(node.left)
            return node

        return dfs(root)
