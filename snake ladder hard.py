import collections


class Solution:
    def minThrow(self, N, nums):
        d = {}
        i = 0
        while i < len(nums) - 1:
            d[nums[i]] = nums[i + 1]

            i += 2

        visited = set()
        visited.add(1)
        q = collections.deque([(1, 0)])
        while q:

            node, dist = q.popleft()

            if node == 30:
                return dist
            j = node + 1
            while j <= node + 6 and j < 31:

                if j not in visited:
                    visited.add(j)
                    new_dist = dist + 1

                    if j in d:
                        new_node = d[j]
                    else:

                        new_node = j

                    q.append((new_node, new_dist))

                j += 1

        return -1