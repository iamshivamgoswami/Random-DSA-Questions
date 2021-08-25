import collections


class Solution:
    def deleteTreeNodes(self, n, parent, value):

        sons=collections.defaultdict(list)
        for i,p in enumerate(parent):
            if i:
                sons[p].append(i)
        def dfs(x=0):
            total,count=value[x],1

            for child in sons[x]:
                t,c=dfs(child)
                total+=t
                count+=c
            return total,count if total else 0


        return dfs()[1]

