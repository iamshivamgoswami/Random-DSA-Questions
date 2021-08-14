import math


class Solution:
    def maxDistance(self, arr: List[List[int]]) -> int:
        res, curr_min, curr_max = 0, math.inf, -math.inf
        for i in arr:
            res = max(res, max(i[-1] - curr_min, curr_max - i[0]))
            curr_min, curr_max = min(curr_min, i[0]), max(curr_max, i[-1])
        return res
