import math


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        diff = math.inf
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if abs(summ - target) < abs(diff):
                    diff = summ - target
                if summ < target:

                    lo += 1
                else:

                    hi -= 1
                if diff == 0:
                    break

        return target + diff

