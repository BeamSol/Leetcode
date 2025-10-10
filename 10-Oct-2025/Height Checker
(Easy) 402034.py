# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        h = sorted(heights)
        for i in range(len(h)):
            if heights[i] != h[i]:
                ans += 1
        return ans