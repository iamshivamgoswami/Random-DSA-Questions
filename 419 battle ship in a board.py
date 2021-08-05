class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(i, j):
            board[i][j] = "."
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "X":
                    dfs(x, y)

        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    dfs(i, j)
                    count += 1
        return count


