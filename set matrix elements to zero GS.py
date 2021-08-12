class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()

        def dfs(i, j):
            matrix[i][j] = 0
            visited.add((i, j))
            for col in range(len(matrix[0])):
                if (i, col) not in visited:
                    dfs(i, col)
            for row in range(len(matrix)):
                if (row, j) not in visited:
                    dfs(row, j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    dfs(i, j)




