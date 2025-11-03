# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        memo = {}
        MOD = 10**9 + 7
        def dp(curr, step):
            if curr == endPos and step == k:
                return 1
            if step > k:
                return 0

            if (curr, step) in memo:
                return memo[(curr, step)]

            ans = (dp(curr-1, step+1) + dp(curr+1, step+1)) % MOD
        
            memo[(curr, step)] = ans
            return ans
        return dp(startPos,0)