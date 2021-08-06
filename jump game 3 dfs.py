class Solution:
    def canReach(self, nums: List[int], start: int) -> bool:
        ans = None

        def func(start, nums):
            if 0 <= start < len(nums) and nums[start] >= 0:
                if nums[start] == 0:
                    return True

                nums[start] = -nums[start]
                return func(start - nums[start], nums) or func(start + nums[start], nums)

        return func(start, nums)



