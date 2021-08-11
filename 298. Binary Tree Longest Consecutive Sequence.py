# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        maxx = 1

        def dfs(node, par=None, count=0):
            nonlocal maxx
            if not node:
                return None

            if par and node.val == par.val + 1:

                maxx = max(count + 1, maxx)

                dfs(node.left, node, count + 1)
                dfs(node.right, node, count + 1)
            else:

                dfs(node.left, node, 1)
                dfs(node.right, node, 1)

        dfs(root)
        return maxx


