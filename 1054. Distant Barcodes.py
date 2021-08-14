import collections


class Solution:
    def rearrangeBarcodes(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        stack = sorted(list(c.items()), key=lambda x: x[1])
        num, freq = stack.pop()
        lst = [[num] for i in range(freq)]
        while stack and stack[-1][1] == freq:
            char, _ = stack.pop()
            for l in lst:
                l.append(char)
        tmp = []
        for k, v in stack:
            for j in range(v):
                tmp.append(k)

        for i, c in enumerate(tmp):
            lst[i % (len(lst) - 1)].append(int(c))
        ans = []
        for i in lst:
            ans.extend(i)
        return ans


