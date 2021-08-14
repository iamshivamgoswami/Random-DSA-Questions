class Solution:
    def findLonelyPixel(self, l: List[List[str]]) -> int:
        def dfs(i, j):
            flag = False
            for row in range(len(l)):
                if row == i:
                    continue
                if l[row][j] == "B":
                    flag=True
            for col in range(len(l[0])):
                if col==j:
                    continue
                if l[i][col]=="B":
                    flag=True
            return 1 if not flag else 0

        count=0
        for i in range(len(l)):
            for j in range(len(l[0])):
                if l[i][j]=="B":
                    count+=dfs(i,j)

        return count


