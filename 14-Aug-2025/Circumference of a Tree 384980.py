# Problem: Circumference of a Tree - https://codeforces.com/gym/102694/problem/A

import sys
import threading
from collections import *
from math import ceil, floor

def string(): return sys.stdin.readline().strip()
def num(): return int(sys.stdin.readline().strip())
def mapstr(): return map(str, sys.stdin.readline().strip().split())
def maps(): return map(int, sys.stdin.readline().strip().split())
def strings(): return sys.stdin.readline().strip().split()
def numsl(): return list(map(int, sys.stdin.readline().strip().split()))

def main():
    n = num()
    graph = defaultdict(list)

    for _ in range(n-1):
        a,b = numsl()
        graph[a].append(b)
        graph[b].append(a)

    def dfs_iterative(start):
        stack = [(start,0)]
        visited = set([start])
        len_=(start,0)
        while stack:
            node,depth = stack.pop()
            if depth > len_[1]:
                len_=(node, depth)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor,depth+1))
        return len_
    node1 = dfs_iterative(1)
    diameter= dfs_iterative(node1[0])[1]
    print(diameter*3)
main()
