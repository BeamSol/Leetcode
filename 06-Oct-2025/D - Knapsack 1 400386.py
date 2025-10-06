# Problem: D - Knapsack 1 - https://atcoder.jp/contests/dp/tasks/dp_d

import threading
from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

n, W = map(int, input().split())
k = []
for _ in range(n):
    k.append(list(map(int, stdin.readline().strip().split() )))
memo = {}
dp = [[0]*(W+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = k[i - 1]
    for cap in range(1, W+1):
        dp[i][cap] = dp[i-1][cap]
        if cap >= w:
            dp[i][cap] = max(dp[i][cap],dp[i-1][cap-w]+v)
print(dp[n][W])

