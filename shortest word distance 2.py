class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = collections.defaultdict(list)
        for i, v in enumerate(wordsDict):
            self.d[v].append(i)

    def shortest(self, w1: str, w2: str) -> int:
        l1 = self.d[w1]
        l2 = self.d[w2]
        one, two = 0, 0
        minn = math.inf
        while one < len(l1) and two < len(l2):
            minn = min(minn, abs(l1[one] - l2[two]))
            if l1[one] < l2[two]:
                one += 1
            else:
                two += 1
        return minn