'''
Problem: House Robber
Link: https://leetcode.com/problems/house-robber/
Tags: Dynamic Programming, Array
'''


class Solution:
    def rob(self, nums: list[int]) -> int:
        a, b = 0, nums[0]

        for i in nums[1:]:
            a, b = b, max(b, a + i)
        return b


res = Solution().rob(
    [1, 2, 3, 1]
)
print(res)
