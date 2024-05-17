'''
Problem: Meeting Schedule II
Link: https://leetcode.com/problems/meeting-rooms-ii/
Tags: Intervals, Array
'''


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x.end)

        days = 1
        ends = [intervals[0].end]
        for interval in intervals[1:]:
            included = False
            for i in range(len(ends)):
                if interval.start >= ends[i]:
                    ends[i] = interval.end
                    included = True
                    break
            if not included:
                days += 1
                ends.append(interval.end)

        return days

    def eval(self, intervals: list[tuple[int, int]]) -> int:
        intervals = [
            Interval(start, end) for start, end in intervals
        ]
        return self.minMeetingRooms(intervals)


res = Solution().eval(
    intervals=[(0, 40), (5, 10), (15, 20)]
)
print(res)
