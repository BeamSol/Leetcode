# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

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
    n,m = numbers()
    if n < m:
        print(-1)
    else:
        ans = n
        temp = n // 2
        if n%2:
            temp+=1
        no2 = temp
        # print(temp)
        while temp % m != 0:    
            if no2:
                no2-=1
                temp+=1
        print(temp)





def main():
    t = 1
    for _ in range(t):
        solve()


main()
#if __name__ == "__main__":
#    threading.Thread(target=main).start()