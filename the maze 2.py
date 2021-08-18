import heapq


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        m = len(maze)
        n = len(maze[0])

        def go(start, directions):
            i, j = start
            ii, jj = directions
            l = 0
            while 0 <= i + ii < m and 0 <= j + jj < n and maze[i + ii][j + jj] != 1:
                i += ii
                j += jj

                l += 1
            return l, (i, j)

        visited = set()
        h = []
        dest = tuple(destination)
        heapq.heappush(h, (0, tuple(start)))
        while h:
            l, curr_node = heapq.heappop(h)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            visited[curr_node] = l
            if curr_node == dest:
                return l
            for directions in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_l, new_start = go(curr_node, directions)
                heapq.heappush(h, (new_l + l, new_start))
        return -1


