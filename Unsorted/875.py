import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def eat(speed: int):
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile/speed)

            return time_taken

        start_speed = math.ceil(sum(piles) / h)
        end_speed = max(piles)

        while start_speed < end_speed:
            curr_speed = (start_speed + end_speed) // 2
            time_taken = eat(curr_speed)

            # print(start_speed, curr_speed, end_speed, time_taken)

            if time_taken > h:
                start_speed = curr_speed + 1
            else:
                end_speed = curr_speed

        return start_speed


res = Solution().minEatingSpeed(
    piles=[2, 2],
    h=2
)
print(res)
