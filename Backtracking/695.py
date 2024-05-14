'''
Problem: Max Area of Island
Link: https://leetcode.com/problems/max-area-of-island/description/
Tags: Backtracking, Matrix, Recursive
'''

class Solution:
    DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        res = 0

        n = len(grid)
        m = len(grid[0])

        def calcArea(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return 0
            
            # Mark as visited
            grid[x][y] = 0
            
            return 1 + sum(
                calcArea(x+i, y+j) for i, j in Solution.DIRECTIONS
            )

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res, calcArea(i, j))
        
        return res

res = Solution().maxAreaOfIsland(
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
)
print(res)
