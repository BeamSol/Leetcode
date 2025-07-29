# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
            else:
                c = 0
            ans = max(ans, c)
        return ans