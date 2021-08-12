# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        maxx = 0

        def func(node):
            nonlocal maxx
            if not node:
                return [0, 0]

            inc, dcr = 1, 1
            if node.left:
                left = func()
                if node.val==node.left.val+1:
                    dcr=left[1]+1
                elif node.val==node.left.val-1:
                    inc=left[0]+1
            if node.right:
                right=func(node.right)
                if node.val==node.right.val+1:
                    dcr=max(dcr,right[1]+1)
                elif node.val==node.right.val-1:
                    inc=max(inc,right[0]+1)

            maxx=max(maxx,dcr+inc-1)
            return [inc,dcr]

        func(root)
        return maxx


