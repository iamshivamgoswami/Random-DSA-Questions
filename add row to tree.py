# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        def dfs(node, count=1):
            if not node:
                return None
            if count == depth - 1:
                tmp = TreeNode(val)
                tmp.left = node.left
                node.left = tmp
                tmp = TreeNode(val)
                tmp.right = node.right
                node.right = tmp
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)

        dfs(root)
        return root

