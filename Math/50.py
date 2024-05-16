'''
Problem: Pow(x, n)
Link: https://leetcode.com/problems/powx-n/
Tags: Math, Recursion
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        def solve():
            if n == 0:
                return 1

            if n & 1:
                # n is odd, compute x * x^(n-1)
                return x * self.myPow(x, n-1)

            # n is even, compute x^(n/2) * x^(n/2)
            t = self.myPow(x, n>>1)
            return t * t
            
        return solve()
