class Solution:
    def subsets(self, s: List[int]) -> List[List[int]]:
        ans=[]
        def solve(pos,tmp=[]):
            ans.append(tmp[:])
            for i in range(pos,len(s)):
                tmp.append(s[i])
                solve(i+1,tmp)
                tmp.pop()

        solve(0)
        return ans
    