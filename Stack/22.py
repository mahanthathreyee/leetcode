'''
Problem: Generate Parentheses
Link: https://leetcode.com/problems/generate-parentheses/description/
Tags: Stack, String, Recursion
'''


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def solve(curr=str(''), o=0, c=0):
            if o == c == n:
                res.append(curr)
                return

            if o <= n:
                solve(curr+'(', o+1, c)
            if c < o:
                solve(curr+')', o, c+1)

        solve()
        return res


res = Solution().generateParenthesis(
    n=3
)
print(res)
