# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(cur):
            if cur == target:
                return 1
            if cur > target:
                return 0
            state = (cur)
            if state in memo:
                return memo[state]
            ans = 0
            for num in nums:
                ans += dp(cur + num)
            memo[state] = ans
            return ans
        return dp(0)
