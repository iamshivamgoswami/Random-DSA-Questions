class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        nums.sort()
        merged = []
        for num in nums:
            if not merged or merged[-1][1] < num[0]:
                merged.append(num)
            else:
                merged[-1][1] = max(merged[-1][1], num[1])
        return merged


