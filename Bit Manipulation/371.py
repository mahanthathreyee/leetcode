'''
Problem: Sum of Two Integers
Link: https://leetcode.com/problems/sum-of-two-integers/
Tags: Bit Manipulation, Math
'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            c = a & b
            a = (a ^ b) & mask
            b = (c << 1) & mask

        return a if a <= 0x7FFFFFFF else ~(a ^ mask)


res = Solution().getSum(
    a=-1,
    b=1
)

print(res)
