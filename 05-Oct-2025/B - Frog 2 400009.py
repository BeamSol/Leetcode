# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

import threading
from collections import defaultdict
from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

n, k =map(int, input().split())
list_ = list(map(int, input().split()))
# memo = defaultdict(int)
dp = [0] * n
dp[-1] = 0
dp[n-2] = abs(list_[n-1]- list_[n-2])
for i in range(n-3,-1,-1):
    ans = float("inf")
    for j in range(1, k+1):
        if i + j <= n-1:
            ans = min(ans, (abs(list_[i]-list_[i+j]) + dp[i+j]))
    dp[i] = ans
print(dp[0])

# def rec(i):
#     if i == 0:
#         return 0
#     if i in memo:
#         return memo[i]
    
#     ans = float("inf")
#     for j in range(1, k+1):
#         if i - j >= 0:
#             ans = min(ans, (abs(list_[i]-list_[i-j]) + rec(i-j)))

#     memo[i] = ans
#     return ans
# print(rec(n-1))

