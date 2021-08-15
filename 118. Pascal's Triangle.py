class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [1]
        res = []
        prev = ans
        for i in range(1, numRows + 1):
            res.append(prev)
            tmp = [1]
            for j in range(len(prev) - 1):
                tmp.append(prev[j] + prev[j + 1])
            tmp.append(1)
            prev = tmp
        return res





