'''
Problem: Set Matrix Zeroes
Link: https://leetcode.com/problems/set-matrix-zeroes/description/
Tags: Matrix, Array
'''

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])

        def setZero(x: int, y: int):
            # Change rows
            for i in range(n):
                matrix[i][y] = 0
            
            # Change columns
            for j in range(m):
                matrix[x][j] = 0

        zero_loc = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_loc.add((i, j))
        
        for i, j in zero_loc:
            setZero(i, j)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix)
print(matrix)
