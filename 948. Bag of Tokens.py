import collections
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        lo = collections.deque(sorted(tokens))
        hi = collections.deque(sorted(tokens, reverse=True))
        count = 1
        score = 0
        maxx = 0
        while count <= len(tokens):

            if power >= lo[0]:
                power -= lo.popleft()
                hi.pop()
                score += 1
            elif score >= 1:
                power += hi.popleft()
                lo.pop()
                score -= 1
            maxx = max(score, maxx)
            count += 1
        return maxx
