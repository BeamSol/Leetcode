# Problem: Can I Square? - https://codeforces.com/contest/1915/problem/C

test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    sums = sum(nums)
    i = 1
    while i*i < sums:
        i+=1
    # print(i,sums)
    if i*i == sums:
        print("YES")
    else:
        print("NO")