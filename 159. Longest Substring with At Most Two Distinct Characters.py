import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        c = collections.defaultdict(int)
        i = 0
        j = 0
        maxx = 1
        while j < len(s):
            c[s[j]] += 1

            if len(c) <= 2:
                maxx = max(j - i + 1, maxx)
            if len(c) > 2:
                while i < j and len(c) > 2:

                    c[s[i]] -= 1
                    if c[s[i]] == 0:
                        del c[s[i]]
                    i += 1
            j += 1
        return maxx






