# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        pro = {node: 0 for node in range(n)}
        pro[start_node] = 1
        visited = set()

        heap = [(-1, start_node)]

        while heap:
            cur_pro, cur_node = heapq.heappop(heap)
            cur_pro = -cur_pro


            if cur_node == end_node:
                return cur_pro

            if cur_node in visited:
                continue
            visited.add(cur_node)

            for child, p in graph[cur_node]:
                temp = p*cur_pro
                if temp > pro[child]:
                    pro[child] = temp
                    heapq.heappush(heap, (-temp, child))
        return 0
