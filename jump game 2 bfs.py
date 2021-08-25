class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @functools.lru_cache()
        def func(pos=0):
            if pos>=len(nums)-1:
                return True
            end=min(pos+nums[pos],len(nums)-1)
            for i in range(pos+1,end+1):
                if func(i):
                    return True
            return False
        return func()
