# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        memo = {}
        def dp(index, curr):
            if index == len(nums):
                return curr
            if (index, curr) in memo:
                return memo[(index, curr)]
            temp1 = dp(index+1, curr^nums[index])
            temp2 = dp(index+1, curr)
            memo[(index, curr)] = temp1 + temp2
            return temp1 + temp2
        return dp(0,0)