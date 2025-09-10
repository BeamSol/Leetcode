# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        r=len(s)-1
        ans=0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "1":
                ans+=r-i
                r-=1
        return ans