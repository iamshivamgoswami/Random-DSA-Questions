import heapq


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:

        h = [(-grid[0][0], 0, 0)]
        cost = 0
        visited = set()
        minn = math.inf

        while h:
            curr_dist, i, j = heapq.heappop(h)
            minn = min(-curr_dist, minn)
            if [i, j] == [len(grid) - 1, len(grid[0]) - 1]:
                return minn
            visited.add((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited:
                    heapq.heappush(h, (-grid[x][y], x, y))
        return -1

