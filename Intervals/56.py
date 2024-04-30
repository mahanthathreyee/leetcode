'''
Problem: Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/
Tags: Intervals, Arrays, Sorting
'''

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []

        start_idx = 0
        end_idx = 1

        for interval in sorted(intervals, key=lambda x: x[start_idx]):
            if res and interval[start_idx] <= res[-1][end_idx]:
                # Inside current interval
                res[-1][end_idx] = max(res[-1][end_idx], interval[end_idx])
            else:
                res += interval,
        
        return res

res = Solution().merge(
    [[1,4],[1,5]]
)
print(res)