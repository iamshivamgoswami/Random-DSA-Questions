import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i, j = 0, 0
        q = collections.deque()

        ans = []
        while j < len(nums):

            while q and q[-1] < nums[j]:
                q.pop()
            q.append(nums[j])
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                ans.append(q[0])
                if q and q[0] == nums[i]:
                    q.popleft()
                i += 1
                j += 1
        return ans


