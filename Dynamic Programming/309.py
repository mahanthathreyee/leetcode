'''
Problem: Best Time to Buy and Sell Stock with Cooldown
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/ # noqa: E501
Tags: Dynamic Programming, Arrays
'''

HOLD = 0
BUY = 1
SELL = 2


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        wallet = [0, -prices[0], 0]

        for price in prices[1:]:
            prev_buy_ = wallet[BUY]
            wallet[BUY] = max(wallet[BUY], wallet[HOLD] - price)
            wallet[HOLD] = max(wallet[HOLD], wallet[SELL])
            wallet[SELL] = prev_buy_ + price

        return max(wallet)


res = Solution().maxProfit(
    [1, 2, 3, 0, 2]
)
print(res)
