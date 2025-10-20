# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

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
    arr = array()
    # if n == k:
    #     print(0)
    temp = []
    for i in range(1, n):
        temp.append(arr[i]-arr[i-1])
    temp.sort()
    ans = 0
    for i in range(n-k):
        ans += temp[i]
    # print(temp)
    print(ans)
def main():
    t = 1
    # t = number()
    for _ in range(t):
        solve()


main()
#if __name__ == "__main__":
#    threading.Thread(target=main).start()