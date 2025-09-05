# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        ans = []
        def splitS(index):
            if index == len(s):
                return len(ans) >= 2

            for i in range(index, len(s)):
                x = int(s[index: i+1]) 
                if not ans or ans[-1] - x == 1:
                    ans.append(x)
                    if splitS(i + 1):
                        return True
                    ans.pop()
            return False
        return splitS(0)