# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(am):
            if am == 0:
                return 0
            temp = float("inf")
            if am in memo:
                return memo[am]
            for i in range(len(coins)):
                if coins[i] <= am:
                    temp = min(temp, 1 + dp(am-coins[i]))
            memo[am] = temp
            return temp
        ans = dp(amount)
        return ans if ans != float("inf") else -1