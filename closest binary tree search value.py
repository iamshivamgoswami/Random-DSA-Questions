# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        minn = [math.inf, None]

        def func(node):
            nonlocal minn
            if not node:
                return
            a, b = minn[0], minn[1]

            if abs(node.val - target) < a:
                minn = [abs(node.val - target), node.val]

            if node.val < target:

                func(node.right)
            else:
                func(node.left)

        func(root)

        return minn[1]