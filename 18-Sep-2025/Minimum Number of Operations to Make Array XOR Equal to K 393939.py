# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        temp = nums[0]
        for i in range(1, len(nums)):
            temp^=nums[i]
        
        return bin(temp^k).count("1")