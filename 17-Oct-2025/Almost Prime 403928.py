# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

from collections import defaultdict, Counter, deque
import math, sys, heapq
import threading
from sys import stdin, stdout, setrecursionlimit
from heapq import heapify, heappop, heappushpop, heappush

# setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)  # Uncomment if recursion depth needed

input = lambda: sys.stdin.readline().strip()
number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: map(int, sys.stdin.readline().strip().split())
string = lambda: sys.stdin.readline().strip()
strings = lambda: input().split()
array = lambda: list(map(int, sys.stdin.readline().strip().split()))
array_set = lambda: set(map(int, sys.stdin.readline().strip().split()))
yn = lambda x: 'YES' if x else 'NO'


def solve():
    def prime_factors(n):
        factors = []
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                count = 0
                while n % i == 0:
                    n //= i
                    count += 1
                factors.append((i, count))
        if n > 1:
            factors.append((n, 1))
        return len(factors)
    n = number()
    ans = 0
    for i in range(2, n+1):
        temp = prime_factors(i)
        if temp == 2:
            ans += 1
    print(ans)


def main():
    t = 1
    # t = number()  
    for _ in range(t):
        solve()


main()