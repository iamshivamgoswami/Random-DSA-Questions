class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        summ = 0
        count = 0
        d[0] = 1
        for i in nums:
            summ += i
            if summ % k in d:
                count += d[summ % k]
            d[summ % k] += 1  # we need sum modulo k not sum

        return count
