import math


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res=[]
        def func(n,start,tmp=[]):
            if tmp:
                res.append(tmp+[n])
            for i in range(start,int(math.sqrt(n))+1):
                if n%i==0:
                    func(n//i,i,tmp+[i])
        func(n,2)
        return res

