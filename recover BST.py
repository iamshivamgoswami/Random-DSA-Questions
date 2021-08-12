class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            return dfs(node.left) + [node.val] + dfs(node.right) if node else []

        def two_swapped(nums):
            n = len(nums)
            x = y = -1
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x, y

        def recover(node, count):
            if node:
                if node.val == x or node.val == y:
                    node.val = y if node.val == x else x
                    count -= 1
                    if count == 0:
                        return

                recover(node.left, count)
                recover(node.right, count)

        nums = dfs(root)
        x, y = two_swapped(nums)
        recover(root, 2)
