# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, p=None, gp=None):
            nonlocal ans
            if not node:
                return
            node.parent = p
            node.grandparent = gp
            if not node.grandparent:
                ans += 0
            if node.grandparent and node.grandparent.val & 1 == 0:
                ans += node.val
            dfs(node.left, node, node.parent)
            dfs(node.right, node, node.parent)

        dfs(root)
        return ans