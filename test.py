class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        def func(nums):

            left, right = 0, 0
            count = 0
            maxx = 0
            if len(nums) == 1:
                return nums[0] == 1
            while right < len(nums):
                if nums[right] == 0:
                    count += 1
                if count == 2:
                    maxx = max(maxx, right - left)
                    left = right
                    count = 1
                right += 1
            if count <= 2:
                maxx = max(right - left, maxx)
            return maxx

        return func(nums)









