class Solution:
    def threeSum(self, nums) :
        res=[]
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i==0 or nums[i-1]!=nums[i]:
                lo=i+1
                hi=len(nums)-1
                while lo<hi:
                    summ=nums[i]+nums[lo]+nums[hi]
                    if summ<0:
                        lo+=1
                    elif summ>0:
                        hi-=1
                    else:
                        res.append([nums[i],nums[lo],nums[hi]])
                        lo+=1
                        hi-=1
                        while lo<hi and nums[lo-1]==nums[lo]:
                            lo+=1
        return res