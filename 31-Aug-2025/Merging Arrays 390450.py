# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n , m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
ans = []
p1 = 0
p2 = 0

while p1 < n and p2 < m:
    if list1[p1] < list2[p2]:
        ans.append(list1[p1])
        p1 += 1
    elif list1[p1] >= list2[p2]:
        ans.append(list2[p2])
        p2 += 1

ans.extend(list1[p1:])
ans.extend(list2[p2:])
ans = " ".join(map(str, ans))
print(ans)
