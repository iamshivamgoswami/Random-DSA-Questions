class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans=0

        for i in range(len(nums)-1,1,-1):
            c=nums[i]
            start=0
            end=i-1
            while start<end:
                summ=nums[start]+nums[end]
                if summ>c:
                    ans+=end-start
                    end-=1
                else:
                    start+=1
        return ans



