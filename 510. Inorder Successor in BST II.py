"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left

            return node
        prev = None
        ans = None

        if not node.parent:
            print(1)
            return None
        while node.parent:
            node = node.parent

        return node


