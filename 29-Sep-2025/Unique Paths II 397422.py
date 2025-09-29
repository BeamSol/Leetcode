# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0
            
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = -1
        dp[0][0] = 1
       
        def check(i,j):
            if 0 <= i < m and 0 <= j < n:
                return dp[i][j] if dp[i][j] != -1 else 0
            return 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if dp[i][j] != -1:
                    dp[i][j] = check(i-1,j) + check(i,j-1)

        return dp[m-1][n-1] if dp[m-1][n-1] != -1 else 0

            