'''
Problem: Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/
Tags: Math, Recursion
'''


class Solution:
    MAX_V = 2 ** 31

    def reverse(self, x: int) -> int:
        n = -1 if x < 0 else 1
        x, y = abs(x), 0

        while x != 0:
            y = (y * 10) + (x % 10)
            x //= 10

        return n * y if y < Solution.MAX_V else 0


res = Solution.reverse(
    x=120
)
print(res)
