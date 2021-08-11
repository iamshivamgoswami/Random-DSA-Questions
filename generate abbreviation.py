class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res=[]
        def func(pos,curr,count):
            if pos==len(word):
                res.append(curr+str(count ) if count>0 else curr)
            else:
                func(pos+1,curr,count+1)
                func(pos+1,curr+(str(count) if count>0 else "")+word[pos],0)

        func(0,"",0)
        return res


