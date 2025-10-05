# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

test = int(input())
for _ in range(test):
    n = int(input())
    reds = list(map(int, input().split()))
    m = int(input())
    blues = list(map(int, input().split()))
 
    redSum = 0
    redmax = 0
    bluemax = 0
    blueSum = 0
 
    for i in range(n):
        redSum += reds[i]
        redmax = max(redmax, redSum)
    for i in range(m):
        blueSum += blues[i]
        bluemax = max(bluemax, blueSum)
 
    print(bluemax+redmax)