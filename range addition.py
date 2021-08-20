class Solution(object):
    def getModifiedArray(self, n, updates):
        ans = [0] * n
        for i, j, v in updates:
            ans[i] += v
            if j + 1 < n:
                ans[j + 1] -= v
        summ = 0
        arr = [0] * n
        for i, v in enumerate(ans):
            summ += v
            arr[i] = summ

        return arr

