import collections


class Solution(object):
    def findLeaves(self, root):
        d = collections.defaultdict(list)

        def func(node):
            if not node:
                return 0
            left = func(node.left)
            right = func(node.right)
            maxx = max(left, right) + 1
            d[maxx].append(node.val)
            return maxx

        res = []
        func(root)
        for i, v in d.items():
            res.append(v)
        return res