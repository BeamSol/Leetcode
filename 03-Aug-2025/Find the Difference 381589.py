# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        countS = Counter(s)
        countT = Counter(t)
        for char in countT:
            if countT[char] != countS.get(char, 0):
                return char
