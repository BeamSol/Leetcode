# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev:
                return [i, prev[diff]]
            prev[num] = i 