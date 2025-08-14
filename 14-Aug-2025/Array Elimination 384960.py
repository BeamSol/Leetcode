# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

from functools import reduce
from collections import defaultdict
from math import gcd

test = int(input())
for _ in range(test):
    n= int(input())
    nums=list(map(int, input().split()))
    cnt = []
    x = 1 
    arr = []
    for i in range(31):
        temp =0
        for num in nums:
            if num & x:          
                temp +=1
        x<<=1
        cnt.append(temp)
    for num in cnt:
        if num != 0:
            arr.append(num)
    res = [1]
    if len(arr):
        a = reduce(gcd, arr)
        for i in range(2, a+1):
            if a%i == 0:
                res.append(i)
    else:
        res = [i for i in range(1,n+1)]
    print(*res)