# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maxx=-sys.maxsize):
            nonlocal count
            if not node:
                return

            if node.val >= maxx:
                count += 1
                maxx = node.val
            dfs(node.left, maxx)

            dfs(node.right, maxx)

        dfs(root)
        return count
