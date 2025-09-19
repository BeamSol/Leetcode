# Problem: All Ancestors of a Node in a Directed Acyclic Graph  - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        # print(graph)
        res = [set() for _ in range(n)]
        visited = set()
        def dfs(node):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in res[node]:
                    res[node].add(neigh)
                    dfs(neigh)
                    res[node].update(res[neigh])
            
        for i in range(n):
            dfs(i)
        return [sorted(list (r)) for r in res]