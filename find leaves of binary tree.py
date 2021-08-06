import collections


class Solution(object):
    def findLeaves(self, root):
        d = collections.defaultdict(list)

        def func(node):
            if not node:
                return 0
            left = func(node.left)
            right = func(node.right)
            max_height = max(left, right) + 1

            d[max_height].append(node.val)
            return max_height

        func(root)
        ret = []
        for v in d.values():
            ret.append(v[:])
        return ret


