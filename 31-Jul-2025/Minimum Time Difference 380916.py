# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = sorted(timePoints)
        hh_mm = []
        ans = float("inf")

        for time in times:
            hh, mm = time.split(":")
            hh_mm.append((int(hh), int(mm)))  

        for i in range(1, len(hh_mm)):
            curr = hh_mm[i][0] * 60 + hh_mm[i][1]
            prev = hh_mm[i-1][0] * 60 + hh_mm[i-1][1]
            temp = curr - prev
            ans = min(ans, temp)

        # Handle the circular difference (last and first)
        first = hh_mm[0][0] * 60 + hh_mm[0][1]
        last = hh_mm[-1][0] * 60 + hh_mm[-1][1]
        circular_diff = (1440 - last + first)
        ans = min(ans, circular_diff)

        return ans
