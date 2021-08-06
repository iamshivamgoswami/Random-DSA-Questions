# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        ans = None
        flag = 0

        def func(node):
            nonlocal flag, ans
            if not node:
                return
            func(node.left)

            if flag == 1:
                ans = node
                flag = 0

            if node == p:
                flag = 1
            func(node.right)

        func(root)
        return ans

