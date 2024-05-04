'''
Problem: Longest Increasing Subsequence
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Tags: Dynamic Programming, Binary Search
'''

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = [nums[0]]
        
        for x in nums[1:]:
            if res[-1] < x: res += x,
            else: res[bisect_left(res, x)] = x
        
        return len(res)

res = Solution().lengthOfLIS(
    [10,9,2,5,3,7,101,18]
)
print(res)
