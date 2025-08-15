# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

from collections import defaultdict
test = int(input())
for _ in range(test):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    myDict = defaultdict(list)
    ans = []
    aSorted = sorted(a)
    b.sort()
    for i in range(n):
        myDict[aSorted[i]].append(b[i])
    for i in range(n):
        ans.append(myDict[a[i]][-1])
        myDict[a[i]].pop()
    print(*ans)