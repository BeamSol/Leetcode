# Problem: Minimum One Bit Operations to Make Integers Zero - https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        memo = {}
        def dp(n):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]

            b = n.bit_length() - 1
            mask = 1 << b
            res = (1 << (b + 1)) - 1 - dp(n ^ mask)

            memo[n] = res
            return res

        return dp(n)
