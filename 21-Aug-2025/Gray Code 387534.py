# Problem: Gray Code - https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans=[]
        for i in range(1<<n):
            ans.append(i^(i>>1))
        return ans
