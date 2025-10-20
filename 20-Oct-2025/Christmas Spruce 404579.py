# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

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
    dic = defaultdict(list)
    for i in range(2, n+1):
        parent = number()
        dic[parent].append(i)
    # print(dic)
    for k,val in dic.items():
        c = 0
        for v in val:
            if v not in dic:
                c+=1
        if c < 3:
            print("No")
            return
    print("Yes")


def main():
    t = 1
    # t = number()
    for _ in range(t):
        solve()


main()
#if __name__ == "__main__":
#    threading.Thread(target=main).start()