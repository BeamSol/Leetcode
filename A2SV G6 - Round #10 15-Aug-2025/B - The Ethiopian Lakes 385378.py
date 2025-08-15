# Problem: B - The Ethiopian Lakes - https://codeforces.com/gym/602812/problem/B

from types import GeneratorType
 
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
 
test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    a = []
    for j in range(n):
        a.append(list(map(int, input().split())))
 
    check = [(-1,0), (1,0), (0, -1), (0, 1)]
    visited = set()
 
    def inbound(r,c):
        return 0 <= r and r < n and 0 <= c and c < m
    @bootstrap
    def dfs(i, j):
        visited.add((i, j))
        summ = a[i][j]
        for new_r, new_c in check:
            row_ = new_r + i
            col_ = new_c + j
            if inbound(row_, col_) and (row_, col_) not in visited and a[row_][col_] != 0:
                summ += yield dfs(row_, col_)
        yield summ
          
    ans = 0
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and a[i][j] != 0:
                val = dfs(i,j)
                ans = max(ans, val)
    print(ans)