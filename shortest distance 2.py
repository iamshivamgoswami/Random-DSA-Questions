import collections
import math


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d=collections.defaultdict(list)
        for i,v in enumerate(wordsDict):
            self.d[v].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        list1,list2=self.d[word1],self.d[word2]
        l,r=0,0
        minn=math.inf
        while l<len(list1) and r<len(list2):
            minn=min(minn,abs(list1[l]-list2[r]))
            if list1[l]<list2[r]:
                l+=1
            else:
                r+=1
        return minn



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
