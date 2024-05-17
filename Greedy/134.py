'''
Problem: Gas Station
Link: https://leetcode.com/problems/gas-station/description/
Tags: Greedy
'''


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)

        surplus, total = 0, 0
        ans = 0

        for i in range(n):
            total += gas[i] - cost[i]
            surplus += gas[i] - cost[i]

            if surplus < 0:
                surplus = 0
                ans = i + 1

        if total >= 0:
            return ans
        return -1


res = Solution().canCompleteCircuit(
    gas=[1, 2, 3, 4, 5],
    cost=[3, 4, 5, 1, 2]
)
print(res)
