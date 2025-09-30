# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        for c in coins:
            for am in range(1,amount+1):
                if am >= c:
                    dp[am] += dp[am-c]
        return dp[amount]