class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            coin = coins[i - 1]
            dp[i][0] = 1

            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coin:
                    dp[i][j] += dp[i][j - coin]

        return dp[n][amount]

res = Solution().change(
    amount = 5, 
    coins = [1,2,5]
)   
print(res) 
