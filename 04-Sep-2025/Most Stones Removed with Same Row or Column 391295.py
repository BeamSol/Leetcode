# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(i, visited, row_map, col_map):
            visited.add(i)
            x, y = stones[i]
            for neighbor in row_map[x]:
                if neighbor not in visited:
                    dfs(neighbor, visited, row_map, col_map)
            for neighbor in col_map[y]:
                if neighbor not in visited:
                    dfs(neighbor, visited, row_map, col_map)

        row_map = {}
        col_map = {}
        for i, (x, y) in enumerate(stones):
            if x not in row_map:
                row_map[x] = []
            if y not in col_map:
                col_map[y] = []
            row_map[x].append(i)
            col_map[y].append(i)

        visited = set()
        num_components = 0
        for i in range(len(stones)):
            if i not in visited:
                dfs(i, visited, row_map, col_map)
                num_components += 1

        return len(stones) - num_components
