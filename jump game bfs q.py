import collections


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q = collections.deque([(0)])
        visited = set()
        visited.add(0)
        while q:
            size = len(q)
            for i in range(len(q)):
                v = q.pop()
                if v == len(nums) - 1:
                    return True
                end = min(len(nums) - 1, v + nums[v])
                for c in range(v + 1, end + 1):
                    if c not in visited:
                        visited.add(c)
                        q.append(c)

        return False

