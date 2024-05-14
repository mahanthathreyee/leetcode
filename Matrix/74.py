from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        col_0 = [row[-1] for row in matrix]
        if (row_idx := bisect_left(col_0, target)) >= n: return False
        if (col_idx := bisect_left(matrix[row_idx], target)) >= m: return False
        
        return matrix[row_idx][col_idx] == target

res = Solution().searchMatrix(
    matrix=[
        [ 1, 3, 5, 7],
        [10,11,16,20],
        [23,30,34,60]],
    target=3
)    
print(res)
