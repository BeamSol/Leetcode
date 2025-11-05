# Problem: k-Factorization - https://codeforces.com/problemset/problem/797/A

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
    n, k = numbers()
    if k == 1:
        print(n)
        return
    i = 2
    ans = []
    while i < n:
        while n%i == 0:
            n = n // i
            ans.append(i)
            if len(ans) == k-1 and n != 1:
                ans.append(n)
                print(*ans)
                return
        i+=1
    if n > 1:
        ans.append(n)
    if len(ans) < k:
        print(-1)
    else:
        print(*ans)
            


def main():
    t = 1
    for _ in range(t):
        solve()


main()
#if __name__ == "__main__":
#    threading.Thread(target=main).start()