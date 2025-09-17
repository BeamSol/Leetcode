# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        i = 0
        def tri(ans, i):
            if i == numRows:
                return ans
            temp = []
            for j in range(i+1):
                if j == 0 or i == j:
                    temp.append(1)
                else:
                    temp.append(ans[i-1][j-1]+ans[i-1][j]) 
            ans.append(temp)
            return tri(ans, i+1)
        return tri(ans, i)