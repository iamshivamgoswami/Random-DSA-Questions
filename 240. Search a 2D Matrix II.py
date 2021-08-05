class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j = len(matrix[0]) - 1
        i = 0
        while i < len(matrix) and j > -1:

            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1

        return False

