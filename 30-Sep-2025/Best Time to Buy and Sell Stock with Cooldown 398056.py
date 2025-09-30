# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, flag):
            if i >= len(prices):
                return 0
            state =(i,flag)
            if state in memo:
                return memo[state]

            temp = dp(i+1, flag)

            if flag:
                temp = max(temp, dp(i+2, not flag) + prices[i]) 
            else:
                temp = max(temp, dp(i+1, not flag) - prices[i]) 

            memo[state]=temp
            return temp
        return dp(0, False)