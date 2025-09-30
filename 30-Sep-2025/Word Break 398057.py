# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if s[i:i+len(w)] == w and dp(i+len(w)):
                    memo[i] = True 
                    return memo[i]
            memo[i] = False  
            return False
        return dp(0)