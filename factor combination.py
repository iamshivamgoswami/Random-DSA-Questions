import math


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1:
            return []
        res=[]
        def func(path=[], rest=2, target=n):
            if path:
                res.append(path+[target])
            for i in range(rest,int(math.sqrt(target)+1)):
                if target%i==0:
                    func(path+[i],i,target//i)


        func()
        return res




