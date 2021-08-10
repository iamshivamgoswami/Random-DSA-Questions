import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lo = 0
        hi = int(math.sqrt(c))
        while lo <= hi:
            summ = lo * lo + hi * hi

            if summ > c:
                hi -= 1
            elif summ < c:
                lo += 1
            else:
                return True

        return False
