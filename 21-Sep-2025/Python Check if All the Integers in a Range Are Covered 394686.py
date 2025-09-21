# Problem: Python Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check=set()
        for x,y in ranges:
            while x <= y:
               check.add(x)
               x+=1
        while left<=right:
            if left not in check:
                return False
            left +=1
            
        return True