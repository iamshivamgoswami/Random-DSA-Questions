class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        one = None
        two = None
        ans = sys.maxsize
        for i, v in enumerate(wordsDict):
            if v == word1:

                one = i
            elif v == word2:

                two = i

            if one != None and two != None:
                ans = min(abs(one - two), ans)

        return ans