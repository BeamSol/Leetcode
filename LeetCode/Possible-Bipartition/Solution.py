class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        check = [0]*(n+1)
        for node1, node2 in dislikes:
            graph[node1].append(node2)
            graph[node2].append(node1)
        # print(graph) 
        def dfs(start):
            stack = [start]
            visitied = set([start])
            check[start] = 1
            while stack:
                node = stack.pop()
                for neighbour in graph[node]:
                    if check[neighbour] == check[node]:
                        return False
                    elif check[node] == 1:
                        check[neighbour] = 2
                    else:
                        check[neighbour] = 1

                    if neighbour not in visitied:
                        stack.append(neighbour)
                        visitied.add(neighbour)
            return True
        
        for i in range(1, n + 1):
            if check[i] == 0:
                if not dfs(i):
                    return False
        return True

            


