# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from heapq import heappop, heappush
import sys
from collections import *
from bisect import *
from types import GeneratorType
def inp(): return sys.stdin.read().strip()
def arr(): return list(map(int, sys.stdin.readline().split()))
def string(): return sys.stdin.readline().strip()
def integer(): 
    return int(sys.stdin.readline())

def solve():
    n, e = arr()
    road = defaultdict(list)
    rail = defaultdict(list)
    s = set()
    for _ in range(e):
        u, v = arr()
        road[u].append((v, 1))
        road[v].append((u, 1))
        s.add((u,v))
        s.add((v,u))

    for i in range(1, n+1):
        for j in range(i + 1, n+1):
            if (i, j) not in s:
                rail[i].append((j, 1))
                rail[j].append((i, 1))
    # print(rail, road)
    
    def sp(start, end, graph):
        
        heap = [(0, start)]
        visited = set()
        ans = float("inf")
        while heap:
            dis, node = heappop(heap)
            if node in visited:
                continue
            if node == n:
                ans = dis

            visited.add(node)
            for child, dist in graph[node]:
                heappush(heap, (dis+dist, child))
       
        return ans 
    temp = max(sp(1, n, road), sp(1, n, rail))
    return temp if temp != float("inf") else -1
    

print(solve())
