# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

import threading
from collections import defaultdict
from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

n =int(input())
list_ = list(map(int, input().split()))
memo = defaultdict(int)
dp = [0] * n
dp[n-1] = 0
dp[n-2] = abs(list_[n-1]- list_[n-2])
for i in range(n-3,-1,-1):
    dp[i] = min(abs(list_[i]-list_[i+1]) + dp[i+1], abs(list_[i]-list_[i+2]) + dp[i+2])

print(dp[0])