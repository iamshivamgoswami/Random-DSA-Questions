class Solution:
    def boldWords(self, words: List[str], s: str) -> str:

        bold = [False] * len(s)
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, len(word) + start):
                    bold[i] = True
                start = s.find(word, start + 1)
        ans = []
        i = 0
        while i < len(s):
            if bold[i]:
                ans.append("<b>")
                while i < len(s) and bold[i]:
                    ans.append(s[i])
                    i += 1
                ans.append("</b>")
            else:
                ans.append(s[i])
                i += 1
        return "".join(ans)
