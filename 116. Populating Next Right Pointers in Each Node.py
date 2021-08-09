"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

import collections


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = collections.deque([root, None])
        ans, level = [], collections.deque()
        while q:
            node = q.popleft()
            if node:
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            else:
                if q:
                    q.append(None)
                ans.append(level)
                level = collections.deque()

        for i in ans:
            prev = i[0]
            i.popleft()
            while i:
                prev.next = i[0]
                prev = i.popleft()

            prev.next = None
        return root








