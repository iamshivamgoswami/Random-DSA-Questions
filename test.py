class Solution:
    def threeSumSmaller(self, nums, target):
        summ = 0
        nums.sort()

        def func(nums, left, target):
            right = len(nums) - 1
            summ = 0
            while left < right:
                if nums[left] + nums[right] < target:
                    summ += right - left

                    left += 1
                else:
                    right -= 1
            return summ

        for i in range(len(nums) - 2):
            summ += func(nums, i + 1, target - nums[i])
        return summ
