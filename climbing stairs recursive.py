import functools


class Solution:
    def climbStairs(self, n: int) -> int:
        @functools.lru_cache()
        def func(i=0):
            if i>n:
                return 0
            if i==n:
                return 1
            return func(i+1)+func(i+2)
        return func()
