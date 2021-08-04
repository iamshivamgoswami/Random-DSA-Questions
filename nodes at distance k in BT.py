# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node,par=None):
            if not node:
                return None
            node.par=par
            dfs(node.left,node)
            dfs(node.right,node)

        dfs(root)
        q=collections.deque([(target,0)])
        seen={target}
        while q:
            if q[0][1]==k:
                return [node.val for node,dist in q]
            curr_node,dist=q.popleft()
            for nei in (curr_node.left,curr_node.right,curr_node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    q.append((nei,dist+1))


        return []





