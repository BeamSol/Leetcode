# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*(query_row + 2) for _ in range((query_row + 2))]
        for i in range(query_row + 1):
            for j in range(i+1):
                if poured >= 1:
                    dp[i][j] = 1
                    poured -= 1
                    dp[i+1][j] += poured / 2
                    dp[i+1][j+1] += poured / 2
                    poured = 0
                if dp[i][j] > 1:
                    rem = dp[i][j] - 1
                    dp[i][j] = 1
                    dp[i+1][j] += rem / 2
                    dp[i+1][j+1] += rem / 2
        return dp[query_row][query_glass]
