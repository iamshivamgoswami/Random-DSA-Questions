import collections
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) % p == 0:
            return 0
        target = sum(nums) % p
        d = collections.defaultdict(int)
        d[0] = -1
        summ = 0
        minn = len(nums)
        for i, v in enumerate(nums):
            summ = (summ+v)%p
            if (summ - target)%p in d:
                minn = min(minn, i - d[(summ - target)%p])
            d[summ] = i
        return minn if minn != len(nums) else -1




