class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def dfs(i,j):
            mine_count=0
            for row,col in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
                if 0<=row<len(board) and 0<=col<len(board[0]) and board[row][col]=="M":
                    mine_count+=1
            if mine_count>0:
                board[i][j]=mine_count
                return
            board[i][j]="B"
            for x,y in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
                if  0<=x<len(board) and 0<=y<len(board[0]) and board[x][y]=="E":
                    dfs(x,y)
        if board[click[0]][click[1]]=="M":
            board[click[0]][click[1]]="X"
            return board
        dfs([click[0]][click[1]])
        return board
