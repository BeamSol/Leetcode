# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        ans = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i, j))
        
        def inbound(i, j):
            return 0 <= i < len(mat) and 0 <= j < len(mat[0])

        while queue:
            r, c = queue.popleft()
            for row, col in directions:
                new_r = row + r
                new_c = col + c
                if inbound(new_r, new_c) and ans[new_r][new_c] == -1:
                    ans[new_r][new_c] = ans[r][c] + 1
                    queue.append((new_r, new_c))
        return ans