import collections
class Solution:
    def leastInterval(self, tasks: List[str], k: int) -> int:
        s = "".join(tasks)

        c = collections.Counter(s)
        stack = sorted(c.items(), key=lambda x: x[1])
        char, count = stack.pop()
        lst = [[char] for i in range(count)]
        while stack and stack[-1][1] == count:
            char, _ = stack.pop()
            for l in lst:
                l.append(char)
        res = "".join(c * n for c, n in stack)
        for i, c in enumerate(res):
            lst[i % (len(lst) - 1)].append(c)
        print(lst)
        Count = 0
        for l in lst[:-1]:
            if len(l) <= k:
                print(l)
                Count += k - len(l) + 1
        return Count + len(s)