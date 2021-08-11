class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        res = 0
        for i in nums:
            cnt = 0
            while i not in visited:
                visited.add(i)
                cnt += 1
                i = nums[i]
            print(visited)
            res = max(res, cnt)

        return res



