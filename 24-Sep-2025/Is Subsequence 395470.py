# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = defaultdict(int)
        def dp(sI,tI):
            if sI >= len(s):
                return True
            if tI >= len(t):
                return False

            state = (sI,tI)
            if state in memo:
                return memo[state]

            if s[sI] == t[tI]:
                res = dp(sI+1, tI+1)
            else:
                res = dp(sI, tI+1)
            
            memo[state] = res
            return res
        return dp(0,0)

