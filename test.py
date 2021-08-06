class Solution:
    def countUnivalSubtrees(self, root):
        self.ans = 0
        def recurse(node, parent):
            if not node:
                return True
            left = recurse(node.left, node.val)
            right = recurse(node.right, node.val)
            if left and right:
                self.ans += 1
            return left and right and node.val == parent
        recurse(root, None)
        return self.ans