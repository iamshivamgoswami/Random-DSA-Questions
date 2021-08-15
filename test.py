class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        return self.func(0,n)

    def func(self,start,end):
        if start>end:
            return [None]
        all_nodes=[]
        for curr_root in range(start,end+1):
            left_tree=self.func(start,curr_root-1)
            right_tree=self.func(curr_root+1,end)
            for l in left_tree:
                for r in right_tree:
                    root=TreeNode(curr_root)
                    root.left=left_tree
                    root.right=right_tree
                    all_nodes.append(root)

        return all_nodes
