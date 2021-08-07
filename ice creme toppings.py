class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

        def func(curr, toppingCosts, index, target):
            nonlocal result
            if abs(target - curr) < abs(target - result) or abs(target - curr) == abs(
                    target - result) and curr < result:
                result = curr
            if index == len(toppingCosts) or curr >= target:
                return
            func(curr, toppingCosts, index + 1, target)
            func(curr + toppingCosts[index], toppingCosts, index + 1, target)
            func(curr + toppingCosts[index] * 2, toppingCosts, index + 1, target)

        result = baseCosts[0]

        for i in baseCosts:
            func(i, toppingCosts, 0, target)
        return result