class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        # back means negative
        def dfs(prev, idx, back, seen):
            if idx in seen:
                return prev != idx
            seen.add(idx)
            if back and nums[idx] > 0:
                return False
            if not back and nums[idx] < 0:
                return False
            return dfs(idx, (idx + nums[idx] + n) % n, back, seen)

        for i, x in enumerate(nums):
            if dfs(-1, i, x < 0, set()):
                return True

        return False
