'''
Problem: Word Search
Link: https://leetcode.com/problems/word-search/
Tags: Matrix, String, Backtracking
'''

POS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = set()
        n = len(board)
        m = len(board[0])
        n_w = len(word)

        def solve(x, y, idx: int=1):
            if idx == n_w: return True
            
            for i, j in POS:
                k, l = x + i, y + j
                if k >= 0 and k < n and l >= 0 and l < m:
                    if board[k][l] == word[idx]:
                        t_, board[k][l] = board[k][l], '#'
                        if solve(k, l, idx+1): return True
                        board[k][l] = t_
            return False
        
        for a in range(n):
            for b in range(m):
                if board[a][b] == word[0]:
                    t, board[a][b] = board[a][b], '#'
                    if solve(a, b): return True
                    board[a][b] = t

        return False

res = Solution().exist(
    board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    word="ABCCED"
)    
print(res)
