class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<3:
            return False
        min_array=[-1]*n
        min_array[0]=nums[0]
        for i in range(1,n):
            min_array[i]=min(nums[i],min_array[i-1])
        stack=[]
        for j in range(n-1,-1,-1):
            if nums[j]<=min_array[j]:
                continue
            while stack and stack[-1]<=min_array[j]:
                stack.pop()
            if stack and stack[-1]<nums[j]:
                return True
            stack.append(nums[j])

        return False
    