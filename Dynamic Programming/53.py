'''
Problem: Maximum Subarray
Link: https://leetcode.com/problems/maximum-subarray/
Tags: Dynamic Programming, Array
'''


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = local = -float('inf')

        for i in nums:
            local = max(i, local + i)
            res = max(res, local)

        return res


res = Solution().maxSubArray(
    nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
)
print(res)
