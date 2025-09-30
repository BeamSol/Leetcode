# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        m = len(grid)
        n = len(grid[0])
        def dp(i,j):
            if i == m-1 and j == n-1:
                return grid[i][j]
            if i == m or j == n:
                return float("inf")
            state = (i,j)
            if state in memo:
                return memo[state]
            temp = grid[i][j] + min(dp(i+1,j),dp(i,j+1))
            memo[state]=temp
            return temp
        return dp(0,0)
            