# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []

        def dfs(node):
            if not node:
                ans.append("None")
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return " ".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = collections.deque(data.split(" "))

        def helper(l):
            if l[0] == "None":
                l.popleft()
                return None
            root = TreeNode(l[0])
            l.popleft()
            root.left = helper(l)
            root.right = helper(l)
            return root

        root = helper(l)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))