class Solution:
    def maxArea(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        maxx = 0

        while lo < hi:
            maxx = (hi - lo) * min(nums[lo], nums[hi])
            if nums[lo] < nums[hi]:
                lo += 1
            else:
                hi -= 1

        return maxx


