# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def GCD(a,b):
            if b == 0:
                return a
            return GCD(b, a%b)
        return GCD(min(nums), max(nums))