# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = defaultdict(int)
        def dp(i):
            if i >= len(nums):
                return 0
            if i not in memo:
                # memo[i] = max(nums[i+2] + dp(i+2), nums[i+2])
                memo[i] =  max(nums[i]+dp(i+2), dp(i+1))
            return memo[i]
        ans = max(dp(0), dp(1))
        return ans