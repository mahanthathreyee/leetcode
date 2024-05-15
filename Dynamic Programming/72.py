'''
Problem: Edit Distance
Link: https://leetcode.com/problems/edit-distance/
Tags: Dynamic Programming, Two Pointer
'''

class Solution:
    POSITIONS = [(1, 0), (0, 1), (1, 1)]

    def minDistance(self, A: str, B: str) -> int:
        n = len(A)
        m = len(B)

        dp = {}
        def solve(x: int=0, y: int=0):
            if x == n and y == m: return 0
            if x == n: return m - y
            if y == m: return n - x

            key = (x, y)
            if key not in dp:
                if A[x] == B[y]: 
                    dp[key] = solve(x + 1, y + 1)
                else:
                    dp[key] = 1 + min(
                        solve(x + i, y + j) for i, j in Solution.POSITIONS
                    )

            return dp[key]
        
        return solve()
    
res = Solution().minDistance(
    A="horse",
    B="ros"
)
print(res)
