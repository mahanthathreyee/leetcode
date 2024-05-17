'''
Problem: Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/
Tags: Intervals, Arrays, Sorting
'''


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ans = []

        start_idx = 0
        end_idx = 1

        for interval in sorted(intervals, key=lambda x: x[start_idx]):
            if ans and interval[start_idx] <= ans[-1][end_idx]:
                # Inside current interval
                ans[-1][end_idx] = max(ans[-1][end_idx], interval[end_idx])
            else:
                ans += interval,

        return ans


res = Solution().merge(
    [[1, 4], [1, 5]]
)
print(res)
