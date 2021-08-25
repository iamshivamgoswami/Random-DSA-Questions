import collections


class Node:
    def __init__(self,n):
        self.val=n
        self.childs=[]
n = Node(20)
n12 = Node(12)
n12.childs = [Node(11), Node(2), Node(3)]
n18 = Node(18)
n18.childs = [Node(15), Node(8)]
n.childs=[n12,n18]
adj=collections.defaultdict(list)
def dfs(node,adj):
    if not node:
        return
    for child in node.childs:
        adj[node.val].extend(dfs(child,adj))
    adj[node.val].extend([node.val])
    return adj[node.val]

dfs(n,adj)
print(adj)