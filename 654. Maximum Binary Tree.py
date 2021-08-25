# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def max_index(arr):
            return max(arr),arr.index(max(arr))
        def func(nums):
            if not nums:
                return None
            val,index=max_index(nums)
            root=TreeNode(val)
            root.left=func(nums[:index])
            root.right=func(nums[index+1:])
            return root
        return func(nums)