class Solution:
    def threeSumSmaller(self, nums, target):
        count=0
        nums.sort()
        def func(nums,left,target):
            right=len(nums)-1
            n=0
            while left<right:
                if nums[left]+nums[right]<target:
                    n+=right-left
                    left+=1
                else:
                    right-=1
            return n

        for  i in range(len(nums)-2):
            count+=func(nums,i+1,target-nums[i])
        return count

