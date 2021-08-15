class Solution:

    def exist(self,board,word):
        self.rows=len(board)
        self.cols=len(board[0])

        self.board=board


        for i in range(self.rows):
            for j in range(self.cols):
                if self.func(i,j,word):
                    return True

        return False

    def func(self,row,col,suffix):
        if len(suffix)==0:
            return True
        if row<0 or row==self.rows or col<0 or col==self.cols or self.board[row][col]!=suffix[0]:
            return False
        self.board[row][col]="#"
        for x,y in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
            res=self.func(x,y,suffix[1:])
            if res:
                return True
        self.board[row][col]=suffix[0]

        return False


