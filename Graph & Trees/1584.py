'''
Problem: Min Cost to Connect All Points
Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
Tags: Graph, MST, Prims
'''


class Solution:
    def minCostConnectPoints(self, P: list[list[int]]) -> int:
        res = 0
        n = len(P)

        dp = [[None] * n for _ in range(n)]

        def dist(i, j):
            if not dp[i][j]:
                dp[i][j] = dp[j][i] = abs(
                    abs(P[i][0] - P[j][0]) + abs(P[i][1] - P[j][1])
                )
            return dp[i][j]

        next_nodes = set(range(1, n))
        next_dist = {i: dist(0, i) for i in range(n)}
        while next_nodes:
            next_iter = iter(next_nodes)
            i = next(next_iter)
            while j := next(next_iter, None):
                if next_dist[i] > next_dist[j]:
                    i = j

            res += next_dist[i]
            next_nodes.remove(i)
            next_dist = {j: min(next_dist[j], dist(i, j)) for j in next_nodes}

        return res


res = Solution().minCostConnectPoints(
    [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
)
print(res)
