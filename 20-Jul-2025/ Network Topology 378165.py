# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict
n, m= map(int, input().split())
graph = defaultdict(list)
cnt = defaultdict(int)
cnt1 = 0
cnt2 = 0
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    cnt[node1] += 1
    cnt[node2] += 1
 
for x,c in cnt.items():
    if c == 1:
        cnt1 += 1
    elif c == 2:
        cnt2 += 1
 
if (cnt1 == n and cnt2 == 0) or (cnt2 == n and cnt1 == 0):
    print("ring topology")
elif cnt2 == m or cnt1 == m:
    print("star topology")  
elif cnt1 == 2 and cnt2 == n-2:
    print("bus topology")
else:
    print("unknown topology")