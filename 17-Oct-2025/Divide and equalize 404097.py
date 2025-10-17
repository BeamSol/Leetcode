# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

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
    def prime_factors(k):
        factors = []
        for i in range(2, int(math.sqrt(k))+ 1):
            count = 0
            if k % i == 0:
                while k % i == 0:
                    count += 1
                    k //= i
                factors.append((i, count))
        if k > 1:
            factors.append((k, 1))
        return factors
    dic = defaultdict(int)
    for num in arr:
        temp = prime_factors(num)
        for k,v in temp:
            dic[k] += v
    # print(dic)
    flag = True
    for k, val in dic.items():
        # print(val)
        if val % n != 0 and val != 0:
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")



def main():
    t = number()
    for _ in range(t):
        solve()


main()
#if __name__ == "__main__":
#    threading.Thread(target=main).start()