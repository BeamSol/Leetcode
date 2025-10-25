# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = defaultdict(int)
        graph = defaultdict(list)

        for i in range(len(original)):
            u = original[i]
            v = changed[i]
            w = cost[i]
            graph[u].append((v,w))

        def short(start, end):
            heap = [(0, start)]
            visited = set()
            ans = inf
            while heap:
                dis, node = heappop(heap)
                if node == end:
                    ans = dis
                    dist[(start,end)]=ans
                    break
                if node in visited:
                    continue
                visited.add(node)  
                
                for v, w in graph[node]:
                    heappush(heap, (dis+w, v))
            return ans
        res = 0
        for i in range(len(source)):
            x = source[i]
            y = target[i]
            if (x, y) in dist:
                res += dist[(x,y)]
            else:
                if short(x, y) == inf:
                    return -1
                res+=short(x, y)
        return res
