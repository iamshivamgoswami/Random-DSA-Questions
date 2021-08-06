class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0

        def func(node, parent=None):

            if not node:
                return True
            left = func(node.left, node.val)
            right = func(node.right, node.val)
            if left and right:
                self.count += 1
            return left and right and node.val == parent

        func(root)
        return self.count






