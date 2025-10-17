# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

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
    n = number()
    arr = array()
    count = 0
    for num in arr:
        while num % 2 == 0:
            count += 1
            num //= 2
    heap = []
    for i in range(n, 0, -1):
        c = 0
        x = i
        while x % 2 == 0 and x > 0:
            c+=1
            x//=2
        heapq.heappush(heap, -c)
    req = n - count
    if req <= 0:
        print(0)
        return 
    else:
        ans = 0
        while heap and req > 0:
            c = -heapq.heappop(heap)
            req -= c
            ans += 1

        print(ans if req <=0 else -1)     



def main():
    t = number()
    for _ in range(t):
        solve()


main()
#if __name__ == "__main__":
#    threading.Thread(target=main).start()