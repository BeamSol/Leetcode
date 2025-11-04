# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        temp = 0
        for i in range(1, len(bank)):
            c1 = bank[i-1].count("1")
            c2 = bank[i].count("1")
            if c1 == 0 and c2 == 0:
                continue
            elif c2 == 0:
                ans += temp*c2
                temp = c1
            elif c1 == 0:
                ans += temp*c2
                temp = c2
            else:
                ans += c1*c2
        return ans
