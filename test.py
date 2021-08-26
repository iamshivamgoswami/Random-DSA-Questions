class Solution:
    def preorder(self, root):
        ans=[]
        self.dfs(root,ans)
        return ans


    def dfs(self,root,ans):
        if not root:
            return []
        ans.append(root.val)
        for child in root.children:
            self.dfs(child,ans)

