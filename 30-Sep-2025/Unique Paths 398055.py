# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1
        def check(i,j):
            if 0 <= i < m and 0 <= j < n:
                return dp[i][j]
            return 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = check(i-1,j) + check(i,j-1)
        return dp[m-1][n-1]
