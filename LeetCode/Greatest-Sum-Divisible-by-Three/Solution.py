class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, tot):
            if i == len(nums):
                return 0 if tot == 0 else float("-inf")
            state = (i, tot)
            if state in memo:
                return memo[state]
            temp = dp(i+1, tot)
            temp = max(temp, nums[i] + dp(i+1, (tot+nums[i])%3))
            memo[state] = temp
            return temp
        return dp(0, 0)