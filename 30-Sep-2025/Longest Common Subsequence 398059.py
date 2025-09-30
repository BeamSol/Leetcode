# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dp(t1, t2):
            if t1 == len(text1) or t2 == len(text2):
                return 0

            state = (t1, t2)

            if state in memo:
                return memo[state]

            if text1[t1] == text2[t2]:
                res=1 + dp(t1+1,t2+1)
            else:
                res=max(dp(t1+1, t2), dp(t1, t2+1))

            memo[state] = res
            return res

        return dp(0,0)
            
            