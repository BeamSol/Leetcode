# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]  
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        c = [0]*n
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    c[i] += 1
        temp = inf
        res = 0
        for i in range(n):
            if c[i] <= temp:
                temp = c[i]
                res = i
        return res

