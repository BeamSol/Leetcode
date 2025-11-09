# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(r):
            if r == n:
                board = []
                for i in range(n):
                    temp = ""
                    for j in range(n):
                        if (i, j) in queen:
                            temp+="Q"
                        else:
                            temp+="."
                    board.append(temp)
                res.append(board)
                return 
            
            for c in range(n):
                if (r + c) in posdiagonal or (r - c) in negdiagonal or (c) in cols:
                    continue
                posdiagonal.add(r+c)
                negdiagonal.add(r-c)
                cols.add(c)
                queen.add((r, c))

                backtrack(r+1)

                posdiagonal.remove(r+c)
                negdiagonal.remove(r-c)
                cols.remove(c)
                queen.remove((r, c))

        res = []
        posdiagonal = set()
        negdiagonal = set()
        cols = set()
        queen = set()
        backtrack(0)
        return res