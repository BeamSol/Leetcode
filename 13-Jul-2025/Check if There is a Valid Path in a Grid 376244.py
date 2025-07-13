# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        dxn = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

        move = {
            1: ['left', 'right'],
            2: ['up', 'down'],
            3: ['left', 'down'],
            4: ['right', 'down'],
            5: ['left', 'up'],
            6: ['right', 'up']
        }

        opposite = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }

        incoming = {
            'up':    [2, 5, 6],
            'down':  [2, 3, 4],
            'left':  [1, 3, 5],
            'right': [1, 4, 6]
        }

        visited = [[False] * n for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True

            for d in move[grid[r][c]]:
                dr, dc = dxn[d]
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if grid[nr][nc] in incoming[opposite[d]]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        return False
