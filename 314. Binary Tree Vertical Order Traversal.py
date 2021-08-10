import collections


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        q.append((root, 0))
        q.append((None, 0))

        d = collections.defaultdict(list)
        while q:
            p = q.popleft()

            curr_node = p[0]
            val = p[1]
            if curr_node:
                d[val].append(curr_node.val)
                if curr_node.left:
                    q.append((curr_node.left, val - 1))
                if curr_node.right:
                    q.append((curr_node.right, val + 1))
            else:

                if q:
                    q.append((None, -1))
        res = []
        for k, v in sorted(d.items()):
            res.append(v)

        return res