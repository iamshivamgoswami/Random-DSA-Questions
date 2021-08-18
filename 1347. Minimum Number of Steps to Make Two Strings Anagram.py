class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = collections.Counter(s)
        for i in t:
            if d[i]:
                d[i] -= 1

        return sum(d.values())

