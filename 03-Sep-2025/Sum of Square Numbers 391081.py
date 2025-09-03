# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c)) + 1):
            b = sqrt(c - i*i)
            if b.is_integer():
                return True
        return False
