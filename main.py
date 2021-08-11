import math
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def func(node):
            if not node:
                return math.inf ,-math.inf ,0
            lmin,lmax,lnum=func(node.left)
            rmin,rmax,rnum=func(node.right)
            n=0
            if node.val>lmax and node.val<rmin:
                n=lnum+rnum+1
                self.res=max(self.res,n)
            return min(node.val,lmin),max(node.val,rmax),n

        func(root)
        return self.res





