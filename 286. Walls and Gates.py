class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        def dfs(i, j, val):
            if rooms[i][j] != 0:
                rooms[i][j] = val

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]):

                    if val + 1 < rooms[x][y] and rooms[x][y] != -1:
                        dfs(x, y, val + 1)

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)




