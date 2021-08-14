class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        import collections

        s = "aaadbbbcc"
        count = collections.defaultdict(int)
        for S in s:
            count[S] += 1
        stack = sorted(list(count.items()), key=lambda x: x[1])
        print(stack)
        char, count = stack.pop()
        lst = [[char] for _ in range(count)]
        print(lst)
        # take care of the letters with same highest freq
        while stack and stack[-1][1] == count:
            char, _ = stack.pop()
            for l in lst:
                l.append(char)

        print(lst)
        # all the characters left
        res = "".join(c * n for c, n in stack)
        print(res)
        # padding
        for i, r in enumerate(res):
            lst[i % (len(lst) - 1)].append(r)#Only letters with the
            # same highest
            # frequency can go in to the last []
        for l in lst[:-1]:
            if len(l) < k:
                return ""
        print(1)
        return ( "".join("".join(l) for l in lst))


