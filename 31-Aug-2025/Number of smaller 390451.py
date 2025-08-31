# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

ans = []
right = 0
for i in range(m):
    while right < n and list1[right] < list2[i]:
        right += 1
    ans.append(right)
print(*ans)
