class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right, p = 0, 0, 1
        count = 0
        while right < len(nums):
            p *= nums[right]
            while left <= right and prod >= k:
                p /= nums[left]
                left += 1
            count += right - left + 1
            right += 1
        return count
