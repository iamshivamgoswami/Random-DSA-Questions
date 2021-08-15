class Solution(object):
    def getModifiedArray(self,n, updates):
        res=[0]*n
        for i in updates:
            start,end,val=i
            res[start]+=val
            if end+1<n:
                res[end+1]-=val

        for i in range(1,n):

            res[i]+=res[i-1]
        return res


