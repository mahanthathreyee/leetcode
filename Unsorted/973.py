import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def euclidiean(x, y):
            return ((x**2) + (y ** 2)) ** 0.5

        res = []
        for x, y in points[:k]:
            heapq.heappush(res, (
                -euclidiean(x, y),
                (x, y)
            ))

        for x, y in points[k:]:
            heapq.heappushpop(res, (
                -euclidiean(x, y),
                (x, y)
            ))

        return list(map(lambda x: x[1], res))


res = Solution().kClosest(
    points=[[1, 3], [-2, 2]],
    k=1
)
print(res)
