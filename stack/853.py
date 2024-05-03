'''
Problem: Car Fleet
Link: https://leetcode.com/problems/car-fleet/description/
Tags: Stack, Monotonic Stack, Sorting
'''

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        res = []
        for pos, speed in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / speed
            if not res or res[-1] < time:
                res.append(time)

        return len(res) 

res = Solution().carFleet(
    target=12,
    position=[10,8,0,5,3],
    speed=[2,4,1,1,3]
)
print(res)
