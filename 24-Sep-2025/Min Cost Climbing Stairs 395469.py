# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo=defaultdict(int)
        def dp(i):
            if i >= len(cost):
                return 0
            if i not in memo:
                memo[i] = cost[i] + min(dp(i+1), dp(i+2))
            return memo[i]
        ans = min(dp(0), dp(1))
        return ans
