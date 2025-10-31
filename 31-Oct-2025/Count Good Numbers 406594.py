# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        q, r = divmod(n, 2)
        return (pow(5,q+r,MOD)*pow(4,q,MOD))%MOD
