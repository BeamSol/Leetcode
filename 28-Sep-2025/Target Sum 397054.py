# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, t):
            if t == 0 and i == len(nums):
                return 1
            if i == len(nums):
                return 0
            state = (i, t)
            if state not in memo:
                temp = dp(i+1, t-nums[i]) + dp(i+1, t+nums[i])
                memo[state] = temp
            return memo[state]

        return dp(0,target)
            
            