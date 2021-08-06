class Solution:

    def jump(self, nums):
        n = len(nums)
        start = 0
        end = 0
        max_end = 0
        step = 0
        if len(nums) <= 1:
            return 0
        while 1:
            step += 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                max_end = max(max_end, i + nums[i])
            start, end = end + 1, max_end

