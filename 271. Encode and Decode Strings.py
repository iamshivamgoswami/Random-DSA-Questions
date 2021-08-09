class Codec:
    def __init__(self):
        self.d = {}

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        n = 0
        s = ""
        flag = False
        for i in strs:
            self.d[n] = i
            if not flag:
                s += str(n)
                flag = True
            else:
                s += "#" + str(n)
            n += 1
        return s

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        l = list(map(int, s.split("#")))
        ans = []
        for i in l:
            ans.append(self.d[i])
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))