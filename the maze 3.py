import heapq


class Solution:
    def findShortestWay(self, maze, ball, hole):
        ball, hole = tuple(ball), tuple(hole)
        Directions = [(1, 0, "d"), (-1, 0, "u"), (0, 1, "r"), (0, -1, "l")]

        def go(x, y, direction):
            xx = x
            yy = y
            i, j, path = direction
            new_dist = 0
            while 0 <= xx + i < len(maze) and 0 <= yy + j < len(maze[0]) and not maze[xx + i][yy + j]:
                xx += i
                yy += j
                new_dist += 1
                if (xx, yy) == hole:
                    break
            return new_dist, path, xx, yy

        h = [(0, "", ball)]
        seen = set()

        while h:
            dis, path, node = heapq.heappop(h)
            if node in seen:
                continue
            if node == hole:
                return path
            seen.add(node)
            for direction in Directions:
                distance, path_new, nei_x, nei_y = go(node[0], node[1], direction)
                nei = (nei_x, nei_y)
                heapq.heappush(h, (distance + dis, path + path_new, nei))
        return "impossible"



