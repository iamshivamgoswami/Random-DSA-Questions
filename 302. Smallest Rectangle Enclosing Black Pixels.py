class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        seen = set()
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:

                if 0 <= x < len(image) and 0 <= y < len(image[0]) and (x, y) not in visited:

                    if image[x][y] == "0":

                        seen.add((i, j))

                    elif image[x][y] == "1":
                        dfs(x, y)

        dfs(x, y)
        min_x, max_x, min_y, max_y = math.inf, -math.inf, math.inf, -math.inf

        for i, j in list(seen):
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)
        count = sum([int(val) for line in image for val in line if val == "1"])

        return (max_x - min_x + 1) * (max_y - min_y + 1) if seen else count

