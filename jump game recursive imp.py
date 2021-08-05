class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @functools.lru_cache()
        def func(pos=0):
            if pos==len(nums)-1:
                return True
            longest_jump=min(pos+nums[pos],len(nums)-1)
            for i in range(pos+1,longest_jump+1):
                if func(i):
                    return True
            return False
        return func()