'''
Problem: Longest Increasing Subsequence
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Tags: Dynamic Programming, Binary Search
'''

from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        ans = [nums[0]]

        for x in nums[1:]:
            if ans[-1] < x:
                ans += x,
            else:
                ans[bisect_left(ans, x)] = x

        return len(ans)


res = Solution().lengthOfLIS(
    [10, 9, 2, 5, 3, 7, 101, 18]
)
print(res)
