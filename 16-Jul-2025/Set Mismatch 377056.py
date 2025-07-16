# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        i = 0
        ans = []
        while i < n:
            curr = nums[i] - 1
            if nums[curr] != nums[i]:
                nums[curr], nums[i] = nums[i], nums[curr]
            else:
                i += 1
                
        for i in range(n):
            if i + 1 != nums[i]:
                return [nums[i], i+1]
                