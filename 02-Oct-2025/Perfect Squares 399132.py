# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        arr = []
        i = 1
        while i * i <= n:
            arr.append(i*i)
            i += 1
        dp = [inf] * (n+1)
        dp[0] = 0
        for i in arr:
            for j in range(1, n+1):
                if j >= i:
                    dp[j] = min(dp[j], dp[j-i] + 1) 
        return dp[n]