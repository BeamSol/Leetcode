class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        unguarded = [[True for _ in range(n)] for _ in range(m)]

        wallsCheck = set((i, j) for i, j in walls)
        guardSet = set((i, j) for i, j in guards)

        for i, j in guards + walls:
            unguarded[i][j] = False

        directions = [(0,1), (0,-1), (-1, 0), (1, 0)]
        def inbound(i,j):
            return 0<=i<m and 0<=j<n

        for i, j in guards:
            for dr, dc in directions:
                r, c = i + dr, j + dc
                while inbound(r, c) and (r, c) not in wallsCheck and (r, c) not in guardSet:
                    unguarded[r][c] = False
                    r += dr
                    c += dc
        ans = 0
        for i in range(m):
            for j in range(n):
               if unguarded[i][j]:
                ans += 1
        return ans
        