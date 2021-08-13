class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        x,y=0,0
        res=[]
        m = {c: [i // 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        for c in target:
            a,b=m[c]
            if b<y:
                res.append("L"*(y-b))
            if a<x:
                res.append("U"*(x-a))
            if a>x:
                res.append("D"*(a-x))
            if b>y:
                res.append("R"*(b-y))
            res.append("!")
            x,y=a,b
        return "".join(res)