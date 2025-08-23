# Problem: Largest Color Value in a Directed Graph - https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        count = [[0] * 26 for _ in range(n)]
        for i in range(n):
            count[i][ord(colors[i]) - ord('a')] = 1

        q = deque([i for i in range(n) if indegree[i] == 0])
        visited = 0
        res = 0

        while q:
            node = q.popleft()
            visited += 1
            res = max(res, max(count[node]))
            
            for nei in graph[node]:
                for c in range(26):
                    count[nei][c] = max(
                        count[nei][c],
                        count[node][c] + (1 if c == ord(colors[nei]) - ord('a') else 0)
                    )
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res if visited == n else -1
