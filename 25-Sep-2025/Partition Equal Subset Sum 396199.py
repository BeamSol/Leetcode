# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2!=0:
            return False
        memo = {}
        def dp(i, s):
            if i < 0:
                return s == 0
            state = (i, s)
            if state not in memo:
                memo[state] = dp(i-1, s) or dp(i-1, s-nums[i])
            return memo[state]
            
        return dp(len(nums)-1, sum_//2)