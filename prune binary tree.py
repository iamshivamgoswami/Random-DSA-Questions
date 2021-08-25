class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def contains_one(node):
            if not node:
                return False
            left_contains_one = contains_one(node.left)
            right_contains_one = contains_one(node.right)

            if not left_contains_one:
                node.left = None

            if not right_contains_one:
                node.right = None

            return node.val or left_contains_one or right_contains_one

        return root if contains_one(root) else None





