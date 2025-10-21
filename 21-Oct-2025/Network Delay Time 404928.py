# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v, w))

        distances = {node: float("inf") for node in range(1, n+1)}
        distances[k] = 0
        visited = set()

        heap = [(0, k)]
        while heap:
            curr_distance, curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue 
            visited.add(curr_node)

            for child, weight in graph[curr_node]:
                dis = weight + curr_distance
                if dis < distances[child]:
                    distances[child] = dis
                    heapq.heappush(heap, (dis, child))

        if len(visited) != n:
            return -1
        else:
            res = float("-inf")
            for key,v in distances.items():
                if key != k:
                    res = max(res, v)
            return res
        