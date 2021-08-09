import math


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        low = -math.inf
        for p in preorder:
            if p <= low:
                return False
            while stack and stack[-1] < p:
                low = stack.pop()
            stack.append(p)

        return True

